from flask import Blueprint, render_template, request, g, session, redirect, url_for
from webapp.user.form import LoginForm
from domain.model.user import User
import subprocess
from domain.model.topic import Category


user_page = Blueprint("user_page", __name__)
@user_page.context_processor
def _():
	g.category = Category.query.filter(Category.parent_id == 0).all()
    return dict(g_category=g.category)

@user_page.route("/user/register", methods=('POST','GET'))
def register():
	
	return render_template('/user/register.html')	


@user_page.route("/user/login", methods=("POST","GET"))
def login():
	
	login_form = LoginForm(request.form)
	if request.method == 'POST':
		if login_form.validate():
			session['user_id'] = login_form.user.id
			return redirect(request.args.get('next') or '/user')

	return render_template("/user/login.html",
			loginform=login_form
		)


@user_page.route("/user/logout")
def logout():

	session.pop('user_id', None)
	return redirect('/user')


@user_page.route("/user")
def user():
	g.info = dir(subprocess)
	return render_template('/user/index.html')	