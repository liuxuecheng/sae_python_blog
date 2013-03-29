# -*- coding: utf-8 -*-
from flask import Flask
from webapp.main.views import main_page
from webapp.mydb.views import db_page
from webapp.user.user import user_page

#app config
app = Flask(__name__)
app.debug = True

#register app
app.register_blueprint(main_page)
app.register_blueprint(db_page)
app.register_blueprint(user_page)
