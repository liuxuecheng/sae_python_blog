from flask import Blueprint
from domain import engine
from domain.model.user import Base

db_page = Blueprint('db_page', __name__)

@db_page.route('/mydb/createdb')
def create_db():
	"""
	create all db
	"""

	from domain.model.user import User
	Base.metadata.create_all(engine) 

	return 'create db'