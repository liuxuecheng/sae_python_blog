from package.wtforms import Form, TextField, validators
from package.wtforms.validators import Required, Length, ValidationError, Email
from domain.model.user import User


class LoginForm(Form):


	def check_email(form, field):
		user_info = User.query.filter(User.email == field.data).first()
		if  user_info is None:
			raise ValidationError('The user does not exist !')


	def check_password(form, field):
		user_info = User.query.filter(User.email == form.email.data).first()
		if  user_info.password != field.data: 
			raise ValidationError('Password is wrong !')


	email = TextField('email', validators=[
			Required('Email not empty!'),
			Email('Email format is wrong !'),
			check_email
		])
	password = TextField('password', validators=[
			Required('password not empty !'),
			Length(min=5, max=18),
			check_password
		])