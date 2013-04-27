# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, g
from domain.model.user import User
from domain import db_session
from domain.model.topic import Category, Topic, TopicTag


main_page = Blueprint('main_page', __name__)


@main_page.context_processor
def _():
	g.category = Category.query.all()
	return dict(code=200)


@main_page.route('/')
def index():
	topic = Topic.query.order_by(Topic.id.desc()).offset(0).limit(10)
	category_ids = [i.category_id for i in topic]
	category = dict((c.id, c) for c in Category.query.filter(Category.id.in_(category_ids)))
	count = dict((t.id, t.count) for t in topic)
	tag = TopicTag.query.all()

	return render_template('/sites/index.html',
		topic = topic,
		count=count,
		category=category,
		tag=tag,
		)


@main_page.route('/about/blog')
def about_blog():
	return render_template('/sites/about.html')


@main_page.route('/about/me')
def about_me():
	return render_template('/sites/me.html')	


@main_page.route('/google6b4228096abe7a0c.html')
def google_websites():
	return render_template('/sites/google6b4228096abe7a0c.html')
