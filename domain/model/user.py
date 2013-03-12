from domain.model import Base
from sqlalchemy import Column, Integer, String

class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	name = Column(String(20))
	password = Column(String(16))

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return "<User('%s','%s')>" %(self.id, self.name)	