# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, g, abort
from domain.model.user import User
from domain import db_session
from domain.model.topic import Category, Topic, TopicTag


topic_page = Blueprint('topic_page', __name__)


@topic_page.context_processor
def _():
	g.category = Category.query.all()
	return dict(code=200)


@topic_page.route('/topic/<int:topic_id>')
def show_topic(topic_id):
	topic = Topic.query.filter(Topic.id == topic_id).first()
	if topic:
		category = Category.query.filter(Category.id == topic.category_id).first()
		topic.count.views += 1
		db_session.commit()
	else:
		abort(404)	

	return render_template('/topic/show.html',
		topic = topic,
		category=category,
		count=topic.count
		)


@topic_page.route('/category/<int:category_id>')
def category(category_id):
	category = Category.query.filter(Category.id == category_id).first()
	topic = Topic.query.filter(Topic.category_id == category_id).all()

	return render_template('/topic/category.html',
		topic = topic,
		category=category
		)


@topic_page.route('/tag/<string:tag_name>')
def category(tag_name=''):
	tag = TopicTag.query.filter(TopicTag.name == tag_name).first()
	topic_tag = TopicToTag.filter(TopicToTag.tag_id == tag.id).all()
	tagids = [t.topic_id for t in topic_tag]
	topic = Topic.gets(tagids)

	return render_template('/topic/category.html',
		topic = topic,
		category=category
		)	