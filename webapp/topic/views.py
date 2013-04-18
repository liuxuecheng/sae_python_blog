# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, g
from domain.model.user import User
from domain import db_session
from domain.model.topic import Category, Topic


topic_page = Blueprint('topic_page', __name__)


@topic_page.context_processor
def _():
	g.category = Category.query.all()
	return dict(code=200)


@topic_page.route('/topic/<int:topic_id>')
def show_topic(topic_id):
	topic = Topic.query.filter(Topic.id == topic_id).first()
	category = Category.query.filter(Category.id == topic.category_id)

	return render_template('/topic/show.html',
		topic = topic,
		category=category,
		)
