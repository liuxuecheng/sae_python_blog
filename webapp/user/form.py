from package.wtforms import Form, TextField, validators

class LoginForm(Form):
	email = TextField('email', validators=[
			Required('Email not empty!')
		])
	password = TextField('password', validators=[
			Required('password not empty')
		])