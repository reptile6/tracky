from flask import Blueprint, flash, render_template, redirect, request, url_for

main = Blueprint('main', __name__)


@main.route('/home', methods=['GET'])
def index():
    return render_template('index.html')
