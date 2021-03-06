# -*- coding: utf-8 -*-
from package.flask_wtf.form import Form
from package.wtforms import TextField, TextAreaField, validators, HiddenField, IntegerField, SelectField
from package.wtforms.validators import Required, Length, ValidationError, Email
from domain.model.topic import Category


class CategoryForm(Form):
	id = HiddenField('id', default=0)
	name = TextField('name', validators=[
		Required(u'分类名称不能为空'),
		Length(min=2, max=20, message=u'分类名称不能太长')
		])


class TopicForm(Form):
	category_data = [(c.id, c.name) for c in Category.query.order_by(Category.id.asc()).all()]

	title = TextField('title',validators=[
		Required(u'标题不能为空')
		])
	content = TextAreaField('content', validators=[
		Required(u'内容不能为空')
		])
	priority = IntegerField('priority', default=0)
	category_id = SelectField('category_id', choices=category_data, coerce=int)
	tag = TextField('tag', default='')