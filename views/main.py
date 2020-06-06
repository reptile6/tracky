from flask import Blueprint, flash, render_template, redirect, request, url_for
from flask_login import current_user

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html', user=current_user)
