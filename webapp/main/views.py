# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, g
from domain.model.user import User
from domain import db_session
from domain.model.topic import Category, Topic


main_page = Blueprint('main_page', __name__)


@main_page.context_processor
def _():
	g.category = Category.query.all()
	return dict(code=200)


@main_page.route('/')
def index():
	topic = Topic.query.offset(0).limit(10)
	return render_template('/sites/index.html',
		topic = topic
		)


@main_page.route('/about')
def about():
	return render_template('/sites/about.html')