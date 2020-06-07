from app import db
from time import sleep
from models import User
from forms import RegistrationForm, LoginForm
from flask_login import login_required, login_user, logout_user
from flask import Blueprint, flash, render_template, redirect, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET'])
def login():
    form = LoginForm(request.form)
    return render_template('login.html', form=form)


@auth.route('/login', methods=['POST'])
def login_post():
    form = LoginForm(request.form)
    username = form.username.data
    password = form.password.data
    user = User.query.filter_by(username=username).first()

    if not user and not check_password_hash(password, form.password.data):
        flash('Please check your login credentials and try again')
        return redirect(url_for('auth.login'))

    login_user(user)

    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET'])
def register():
    form = RegistrationForm(request.form)
    return render_template('register.html', form=form)


@auth.route('/register', methods=['POST'])
def register_post():
    form = RegistrationForm(request.form)
    if form.validate():
        username = form.username.data
        user = User.query.filter_by(username=username).first()
        if user:
            flash('User already exits!')
            sleep(2)
            return redirect(url_for('auth.login'))

        user = User(username=form.username.data, email=form.email.data,
                    password=generate_password_hash(form.password.data, method='sha256'))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))

    return render_template('register.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
