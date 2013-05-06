# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, jsonify, request, redirect
from domain.model.user import User
from domain.model.topic import Category, Topic, TopicTag, TopicToTag
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
			db_session.add(category)
			db_session.commit()
		data['code'] = 200
	else:				
		data['code'] = 401
		data['errors'] = category_form.errors	
	
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
@admin_page.route('/admin/topic/add/<int:id>', methods=("POST","GET"))
@login_required
@is_admin
def add(id = 0):
	topic = Topic.query.filter(Topic.id == id).first()
	topic_form = TopicForm(obj = topic)

	if request.method == 'POST' and topic_form.validate():
		if topic:
			if topic.category_id != topic_form.category_id.data:
				new_category = Category.get(topic_form.category_id.data)
				new_category.num += 1
				old_category = Category.get(topic.category_id)
				old_category.num -= 1

			tag_list = topic_form.tag.data.split(" ")
			for tag_name in tag_list:
				if tag_name.strip():
					tag = TopicTag.query.filter(TopicTag.name == tag_name).first()
					if tag:
						topic_to_tag = TopicToTag.query.filter(TopicToTag.topic_id == id).filter(TopicToTag.tag_id == tag.id).first()
						if topic_to_tag is None:
							tag.num += 1
							topic_to_tag = TopicToTag(id, tag.id)
							db_session.add(topic_to_tag)
					else:
						tag = TopicTag(tag_name)
						db_session.add(tag)	
						db_session.flush()
						topic_to_tag = TopicToTag(topic.id, tag.id)
						db_session.add(topic_to_tag)
								
			topic_form.populate_obj(topic)
			db_session.commit()	
		else:
			topic = Topic(topic_form.title.data)
			topic.content = topic_form.content.data
			topic.category_id = topic_form.category_id.data
			topic.tag = topic_form.tag.data
			db_session.add(topic)
			db_session.flush()

			category = 	Category.get(topic_form.category_id.data)
			category.num += 1
			tag_list = topic_form.tag.data.split(" ")
			for tag_name in tag_list:
				if tag_name.strip():
					tag = TopicTag.query.filter(TopicTag.name == tag_name).first()
					if tag:
						tag.num += 1
					else:
						tag = TopicTag(tag_name)
						db_session.add(tag)
						db_session.flush()
					topic_to_tag = TopicToTag(topic.id, tag.id)
					db_session.add(topic_to_tag)	
			db_session.commit()	
		return redirect('/admin/topic/list')
	else:
		return render_template('/admin/addtopic.html',
			topic_form = topic_form,
			)