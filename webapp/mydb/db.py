from flask import Blueprint
from domain import engine, session
from domain.model import Base

db_page = Blueprint('db_page', __name__)

@db_page.route('/mydb/createdb')
def create_db():
	"""
	create all db
	"""

	from domain.model.user import User
	Base.metadata.create_all(engine) 

	return 'create db'


@db_page.route('/mydb/data')
def init_data():
	"""
	init data
	"""	
	from domain.model.user import User

	user = User("fainle")
	user.password = "123456"

	session.add(user)
	session.commit()