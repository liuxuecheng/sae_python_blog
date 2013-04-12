from flask import Blueprint, render_template, g
from domain.model.user import User
from domain import db_session
from domain.model.topic import Category


main_page = Blueprint('main_page', __name__)


@main_page.context_processor
def _():
	g.category = Category.query.filter(Category.parent_id == 0).all()
	return dict(code=200)

@main_page.route('/')
def index():
	user_info = User.query.all()
	#user_info = db_session.query(User).all()
	return render_template('/sites/index.html')


@main_page.route('/about')
def about():
	return render_template('/sites/about.html')