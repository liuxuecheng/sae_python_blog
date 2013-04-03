from flask import Blueprint, render_template, request, g
from webapp.user.form import LoginForm


user_page = Blueprint("user_page", __name__)


@user_page.route("/user/register", methods=('POST','GET'))
def register():
	return render_template('/user/register.html')	


@user_page.route("/user/login", methods=("POST","GET"))
def login():
	
	login_form = LoginForm(request.form)
	if request.method == 'POST':
		if login_form.validate():
			g.user = 1
	
	return render_template("/user/login.html",
			loginform=login_form
		)


@user_page.route("/user/logout", methods=('GET'))
def logout():
	pass