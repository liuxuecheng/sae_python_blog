from flask import Blueprint

db_page = Blueprint('db_page', __name__)

@db_page.route('/mydb/createdb')
def create_db():
	return 'create db'