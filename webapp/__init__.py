# -*- coding: utf-8 -*-
from flask import Flask
from webapp.main.views import main_page
from webapp.mydb.db import db_page
from webapp.user.views import user_page

#app config
app = Flask(__name__)
app.config.from_pyfile('setting.ini')
app.config.from_envvar('SETTING', silent=True)

#register app
app.register_blueprint(main_page)
app.register_blueprint(db_page)
app.register_blueprint(user_page)

#app before request
@app.before_request
def before_request(exception=None):
	pass


#app teardown request
@app.teardown_request
def teardown_request(exception=None):
	pass		