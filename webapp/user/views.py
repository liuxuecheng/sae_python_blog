from flask import Blueprint, render_template

user_page = Blueprint("user_page", __name__)

@user_page.route("/user/login", methods=("POST","GET"))
def login():

	return render_template("/user/login.html")


@user_page.route("/user/register", methods=('POST','GET'))
def register():
	
	return render_template('/user/register.html')	