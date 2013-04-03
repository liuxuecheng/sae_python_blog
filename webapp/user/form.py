# -*- coding: utf-8 -*-
from package.wtforms import Form, TextField, validators
from package.wtforms.validators import Required, Length, ValidationError, Email
from domain.model.user import User
from flask import flash


class LoginForm(Form):
	email = TextField('email', validators=[
			Required('Email not empty!'),
			Email('Email format is wrong !'),
		])
	password = TextField('password', validators=[
			Required('password not empty !'),
			Length(min=5, max=18),
		])


	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)
		self.user = None


	def validate(self):
		"""
		Validate user email and password is correct.
		"""

		if not Form.validate(self):
			return False
		
		user = User.query.filter(User.email == self.email.data).first()

		if user is not None:
			if user.password == self.password.data:
				self.user = user
				is_user_valid = True
			else:
				self.user = None
				is_user_valid = False
				flash(u'邮箱或密码错误','error')

		else:
			self.user = None
			is_user_valid = False
			flash(u'邮箱或密码错误','error')

		return is_user_valid