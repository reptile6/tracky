from app import db
from models import Task
from flask import Blueprint, flash, render_template, redirect, request, url_for
from flask_login import login_required, current_user

tasks = Blueprint('tasks', __name__)


@tasks.route('/tasks', method=['GET'])
@login_required
def tasks():
    return render_template(url_for('tasks.html'))


@tasks.route('/tasks', methods=['GET'])
@login_required
def get_all_tasks():
    user_id = current_user.id
    tasks_list = Task.query.filter_by(user_id=user_id).all()

    tasks_list = [x for x in tasks_list if x.status != 'closed']

    return tasks_list


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

    return
