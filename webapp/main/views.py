from flask import Blueprint, render_template
from domain.model.user import User

main_page = Blueprint('main_page', __name__)


@main_page.route('/')
def index():
	user_info = User.query.all()
    return render_template('/sites/index.html')


@main_page.route('/about')
def about():
	return render_template('/sites/about.html')