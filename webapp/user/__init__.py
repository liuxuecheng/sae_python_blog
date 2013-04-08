from functools import wraps 
from flask import g, request, redirect, abort


def login_required(func):
	@wraps(func)
	def _(*args, **kwargs):
		if g.user is None:
			return redirect('/user/login', next = request.path)
		return func(*args, **kwargs)

	return _


def is_admin(func):
	@wraps(func)
	def _(*args, **kwargs):
		if g.user is None or g.user.id != 1:
			return abort(404)
		return func(*args, **kwargs)
	
	return _						