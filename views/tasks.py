from app import db
from models import Task
from flask import Blueprint, flash, render_template, redirect, request, url_for
from flask_login import login_required, current_user

tasks = Blueprint('tasks', __name__)


@tasks.route('/tasks', methods=['GET'])
@login_required
def get_all_tasks():
    user_id = current_user.id
    tasks_list = Task.query.filter_by(user_id=user_id).all()

    tasks_list = [x for x in tasks_list if x.status != 'closed']

    return render_template('tasks.html', tasks_list=tasks_list, user=current_user)


@tasks.route('/tasks', methods=['POST'])
@login_required
def create_task():
    user_id = current_user.id
    type = request.form.get('type')
    description = request.form.get('description')
    status = 'OPEN'

    task = Task(user_id=user_id, type=type, description=description, status=status)

    db.session.add(task)
    db.session.commit()


@tasks.route('/tasks/<int:identifier>', methods=['DELETE'])
@login_required
def remove_task(identifier):
    task = Task.query.filter_by(id=identifier).first()

    if not task:
        flash('There is no task associated with that id.')
        return redirect(url_for('tasks.tasks'))

    Task.query.filter_by(id=task.id).delete()
    db.session.commit()

