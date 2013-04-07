from flask import Blueprint, render_template
from domain.model.user import User
from domain import db_session
from webapp.user import login_required, is_admin 


admin_page = Blueprint('admin_page', __name__)


@admin_page.route('/admin')
@admin_page.route('/admin/index')
@login_required
@is_admin
def index():
	return render_template('/admin/index.html')


@admin_page.route('/admin/topic/category')
def category():
	return render_template('/admin/category.html')