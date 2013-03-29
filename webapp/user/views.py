from Flask import Buleprint, render_template

user_page = Buleprint("user_page", __name__)

@user_page.route("/user/login", methods=("POST","GET"))
def login():

	return render_template("/user/login.html")