# -*- coding: utf-8 -*-
from flask import Blueprint
from domain import engine, db_session
from domain.model import Base
import os

db_page = Blueprint('db_page', __name__)

@db_page.route('/mydb/createdb')
def create_db():
	"""
	create all db
	"""

	from domain.model.user import User
	Base.metadata.create_all(engine) 

	return 'create db'


@db_page.route('/mydb/data')
def init_data():
	"""
	init data
	"""	
	from domain.model.user import User

	user = User("hehehas@gmail.com")
	user.nickname = 'fainle'
	user.password = "123456"

	db_session.add(user)
	db_session.commit()


@db_page.route('/mydb/test')
def os_test():
	return dir(os)
	#for i in os.popen('ls -al'):
		#print i