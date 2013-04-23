# -*- coding: utf-8 -*-
from flask import Blueprint
from domain import engine, db_session
from domain.model import Base
import hashlib


db_page = Blueprint('db_page', __name__)


@db_page.route('/mydb/createdb')
def create_db():
	"""
	create all db
	"""

	from domain.model.user import User
	from domain.model.topic import Topic, Category, TopicTag, TopicCount
	Base.metadata.create_all(engine) 

	return 'create db'


@db_page.route('/mydb/data')
def init_data():
	"""
	init data
	"""	
	from domain.model.user import User

	sha1 = hashlib.sha1()
	sha1.update('123456')

	user = User("hehehas@gmail.com")
	user.nickname = 'fainle'
	user.password = sha1.hexdigest()

	db_session.add(user)
	db_session.commit()