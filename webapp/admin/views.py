from flask import Blueprint, render_template, jsonify
from domain.model.user import User
from domain.model.topic import Category, Topic, TopicTag
from domain import db_session
from webapp.user import login_required, is_admin
from webapp.admin.form import CategoryForm 


admin_page = Blueprint('admin_page', __name__)


@admin_page.route('/admin')
@admin_page.route('/admin/index')
@login_required
@is_admin
def index():
	return render_template('/admin/index.html')


@admin_page.route('/admin/topic/category')
@login_required
@is_admin
def category():
	category_form = CategoryForm()
	return render_template('/admin/category.html',
		category_form = category_form	
		)


@admin_page.route('/admin/topic/addcategory')
@login_required
@is_admin
def add_category():
	data = {}
	return jsonify(data)


@admin_page.route('/admin/topic/editcategory')
@login_required
@is_admin
def edit_category():
	pass


@admin_page.route('/admin/topic/delcategory')
@login_required
@is_admin
def del_category():
	pass	