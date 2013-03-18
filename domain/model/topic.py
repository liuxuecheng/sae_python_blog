from domain.model import Base
from sqlalchemy import Column, Integer, String

class Topic(Base):
	"""
	topic model
	"""

	__tablename__ = 'topic'

	id = Column(Integer, primary_key=True)
	title = Column(String(20))
	content = Column(String(16))

	def __init__(self, name):
		self.title = title

	def __repr__(self):
		return "<topic('%s','%s')>" %(self.id, self.title)


class TopicTag(Base):
	"""
	topic tag model
	"""

	__tablename__ = 'topic_tag'

	def __init__:
		pass