# -*- coding: utf-8 -*-
from package.flask_wtf.form import Form
from package.wtforms import TextField, TextAreaField, validators, HiddenField, IntegerField
from package.wtforms.validators import Required, Length, ValidationError, Email


class CategoryForm(Form):
	id = HiddenField('id', default=0)
	name = TextField('name', validators=[
		Required(u'分类名称不能为空'),
		Length(min=2, max=20, message=u'分类名称不能太长')
		])


class TopicForm(Form):
	title = TextField('title', default='')
	content = TextAreaField('content', default='')
	priority = IntegerField('priority', default=0) 	