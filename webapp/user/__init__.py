from functools import wraps 
from flask import g, request, redirect, abort

def login_required(func):
	@wraps(func)
	def _(*args, **kwargs):
		if g.user.get(id) is None:
			return abort(404)
			#return redirect('/user/login')
		return func(*args, **kwargs)

	return _	