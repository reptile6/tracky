from app import db
from time import sleep
from models import User
from flask_login import login_required, login_user, logout_user
from flask import Blueprint, flash, render_template, redirect, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()

    if not user and not check_password_hash(user.password, password):
        flash('Please check your login credentials and try again')
        return redirect(url_for('auth.login'))

    login_user(username)

    return redirect(url_for('main.home'))


@auth.route('/register', methods=['GET'])
def register():
    return render_template('register.html')


@auth.route('/register', methods=['POST'])
def register_post():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()

    if user:
        flash('User already exits!')
        sleep(2)
        return redirect(url_for('auth.login'))

    user = U3ser(username=username, email=email, password=generate_password_hash(password, method='sha256'))
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))