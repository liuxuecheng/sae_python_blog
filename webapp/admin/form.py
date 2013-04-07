# -*- coding: utf-8 -*-
from package.wtforms import Form, TextField, validators, HiddenField, IntegerField
from package.wtforms.validators import Required, Length, ValidationError, Email


class CategoryForm(Form):
	id = HiddenField('id', default=0)
	parent_id  = IntegerField('parent_id', default=0)
	name = TextField('name', default='')
	priority = IntegerField('priority', default=0)