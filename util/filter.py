# -*- coding: utf-8 -*-

def register_jinja_filter(jinja_env):

	jinja_env.filters['string_split'] = string_split


def string_split(s, spstr=None):
	new_list = s.split(spstr)
	return new_list