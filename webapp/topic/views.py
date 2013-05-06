# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, g, abort, request, jsonify
from domain.model.user import User
from domain import db_session
from domain.model.topic import Category, Topic, TopicTag, TopicToTag, TopicReply
from webapp.user import login_required
from webapp.topic.form import ReplyForm


topic_page = Blueprint('topic_page', __name__)


@topic_page.context_processor
def _():
	g.category = Category.query.all()
	return dict(code=200)


@topic_page.route('/topic/<int:topic_id>')
def show_topic(topic_id):
	topic = Topic.query.filter(Topic.id == topic_id).first()
	reply_form = ReplyForm()
	if topic:
		category = Category.query.filter(Category.id == topic.category_id).first()
		topic.count.views += 1
		db_session.commit()
	else:
		abort(404)	

	return render_template('/topic/show.html',
		topic = topic,
		category=category,
		count=topic.count,
		reply_form=reply_form
		)


@topic_page.route('/category/<int:category_id>')
def category(category_id=0):
	category = Category.query.filter(Category.id == category_id).first()
	topic = Topic.query.filter(Topic.category_id == category_id).all()

	return render_template('/topic/category.html',
		topic = topic,
		category=category
		)


@topic_page.route('/tag/<string:tag_name>')
def tag(tag_name=''):
	tag = TopicTag.query.filter(TopicTag.name == tag_name).first()
	topic_tag = TopicToTag.query.filter(TopicToTag.tag_id == tag.id).all()
	tagids = [t.topic_id for t in topic_tag]
	topic = Topic.gets(tagids)

	return render_template('/topic/tag.html',
		topic = topic,
		tag=tag,
		category=category
		)


@topic_page.route("/topic/reply", methods=("POST","GET"))
@login_required
def add_reply():
	data = {}
	id = request.form['id']
	reply = TopicReply.query.filter(TopicReply.id == id).first()
	reply_form = ReplyForm(obj = reply)
	if request.method == 'POST' and reply_form.validate():
		if reply:
			reply_form.populate_obj(reply)
			db_session.commit()
			data['code'] = 200
		else:
			reply = TopicReply(reply_form.content.data)
			reply.user_id = reply_form.user_id.data
			reply.topic_id = reply_form.topic_id.data
			topic = Topic.get(reply_form.topic_id.data)
			topic.count.reply_num += 1
			db_session.add(reply)
			db_session.commit()
			data['code'] = 200
	else:				
		data['code'] = 401
		data['errors'] = reply_form.errors	
	return jsonify(data)