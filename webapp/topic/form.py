# -*- coding: utf-8 -*-
from package.wtforms import Form, TextField, validators, HiddenField, TextAreaField
from package.wtforms.validators import Required, Length, ValidationError, Email, EqualTo


class ReplyForm(Form):
	user_id = HiddenField('user_id', validators=[
			Required(u'user_id不能为空!'),
		])
	topic_id = HiddenField('topic_id', validators=[
			Required(u'topic_id不能为空!'),
		])
	content = TextAreaField('content',validators=[
			Required(u'留言内容不能为空!'),
		])