# -*- coding: utf-8 -*-

def register_jinja_filter(jinja_env):

	jinja_env.filters['string_split'] = string_split


def string_split(s, str=''):
	new_list = s.split(str)
	return new_list