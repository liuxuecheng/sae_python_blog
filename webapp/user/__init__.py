from functools import wraps 
from flask import g, request, redirect

def login_required(func):
	@wraps(func)
	def _(*args, **kwargs):
		if g.user is None:
			return redirect('/user/login')
		return func(*args, **kwargs)

	return _	