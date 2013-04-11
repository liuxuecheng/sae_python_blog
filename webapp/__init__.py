# -*- coding: utf-8 -*-
from flask import Flask, g, session
from webapp.mydb.db import db_page
from webapp.main.views import main_page
from webapp.user.views import user_page
from webapp.admin.views import admin_page
from domain import db_session
from domain.model.user import User
from domain.model.topic import Category


#app config
app = Flask(__name__)
app.config.from_pyfile('setting.ini')
app.config.from_envvar('SETTING', silent=True)


#register blueprint
app.register_blueprint(main_page)
app.register_blueprint(db_page)
app.register_blueprint(user_page)
app.register_blueprint(admin_page)


#app before request Category
@app.before_request
def before_request():
	if 'user_id' in session:
		g.user = User.query.filter(User.id == session['user_id']).first()
	else:
		g.user = None

	#g.category = Category.query.filter(Category.parent_id == 0).all()		


#app teardown request
@app.teardown_request
def shutdown_session(exception=None):
	db_session.remove()
	db_session.close() 		