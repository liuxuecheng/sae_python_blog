from flask import Blueprint, render_template, request, g, session, redirect
from webapp.user.form import LoginForm
from domain.model.user import User


user_page = Blueprint("user_page", __name__)


@user_page.route("/user/register", methods=('POST','GET'))
def register():
	return render_template('/user/register.html')	


@user_page.route("/user/login", methods=("POST","GET"))
def login():

	login_form = LoginForm(request.form)
	if request.method == 'POST':
		if login_form.validate():
			session['user_id'] = login_form.user.user_id
			return redirect('/user')

	return render_template("/user/login.html",
			loginform=login_form
		)


@user_page.route("/user/logout", methods=('GET'))
def logout():
	pass


@user_page.route("/user")
def user():
	if 'user_id' in session:
		user = User.query.filter(User.id == session['user_id']).first()
	else:
		user = []	
	return render_template('/user/index.html',
			user = uesr
		)	