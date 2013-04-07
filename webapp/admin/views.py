from flask import Blueprint, render_template
from domain.model.user import User
from domain import db_session

admin_page = Blueprint('admin_page', __name__)


@admin_page.route('/admin')
@admin_page.route('/admin/index')
def index():
	user_info = User.query.all()
	#user_info = db_session.query(User).all()
	return render_template('/admin/index.html')


@admin_page.route('/admin/topic/category')
def category():
	return render_template('/admin/category.html')