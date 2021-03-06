# -*- coding: utf-8 -*-
from package.flask_wtf.form import Form
from package.wtforms import TextField, validators, HiddenField, TextAreaField
from package.wtforms.validators import Required, Length, ValidationError, Email, EqualTo


class ReplyForm(Form):
	id = HiddenField('id')
	user_id = HiddenField('user_id', validators=[
			Required(u'user_id不能为空!'),
		])
	topic_id = HiddenField('topic_id', validators=[
			Required(u'topic_id不能为空!'),
		])
	content = TextAreaField('content',validators=[
			Required(u'留言内容不能为空!'),
		])