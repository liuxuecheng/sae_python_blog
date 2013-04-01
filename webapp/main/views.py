from flask import Blueprint, render_template

main_page = Blueprint('main_page', __name__)


@main_page.route('/')
def index():
    return render_template('/sites/index.html')


@main_page.route('/about')
def about():
	return render_template('/sites/about.html')