# -*- coding: utf-8 -*-
from package.wtforms import Form, TextField, validators
from package.wtforms.validators import Required, Length, ValidationError, Email


class CategoryForm(Form):