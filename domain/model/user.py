from domain.model import Base
from sqlalchemy import Column, Integer, String

class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	password = Column(String)

	def __init__(self, id, name):
		self.id = id
		self.name = name

	def __repr__(self):
		return "<User('%s','%s')>" %(self.id, self.name)	