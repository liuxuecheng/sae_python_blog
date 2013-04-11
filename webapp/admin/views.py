from flask import Blueprint, render_template, jsonify, request
from domain.model.user import User
from domain.model.topic import Category, Topic, TopicTag
from domain import db_session
from webapp.user import login_required, is_admin
from webapp.admin.form import CategoryForm, TopicForm 


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
	category = Category.query.all()
	category_form = CategoryForm()
	return render_template('/admin/category.html',
		category=category,
		category_form = category_form	
		)


@admin_page.route("/admin/topic/addcategory", methods=("POST",)) 
@login_required
@is_admin
def add_category():
	data = {}
	id = request.form['id']
	category = Category.query.filter(Category.id == id).first()
	category_form = CategoryForm(obj = category)
	if request.method == 'POST' and category_form.validate():
		if category:
			category_form.populate_obj(category)
			db_session.commit()
		else:
			category = Category(category_form.name.data)
			category.parent_id = category_form.parent_id.data
			category.priority = category_form.priority.data
			db_session.add(category)
			db_session.commit()
		data['code'] = 200
	else:				
		data['code'] = 401	
	
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


@admin_page.route('/admin/topic/add', methods=("POST","GET"))
@login_required
@is_admin
def add():
	id = request.form['id']
	topic = Topic.query.filter(Topic.id == id).first()
	return topic
	topic_form = TopicForm(obj = topic)
	return render_template('/admin/addtopic.html',
		topic_form = topic_form,
		)		