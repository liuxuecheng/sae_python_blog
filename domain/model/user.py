from domain.model import Base
from sqlalchemy import Column, Integer, String

class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	email=Column(String(50))
	nickname = Column(String(20))
	password = Column(String(16))

	def __init__(self, email):
		self.name = email

	def __repr__(self):
		return "<User('%s','%s')>" %(self.id, self.email)	