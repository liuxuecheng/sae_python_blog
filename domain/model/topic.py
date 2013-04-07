from domain.model import Base
from sqlalchemy import Column, Integer, String, Text


class Category(Base):
	"""
	Category model
	"""
	__tablename__ = 'topic_category'
	id = Column(Integer, primary_key=True)
	parent_id = Column(Integer, default=0)
	name = Column(String(20), default='')
	priority = Column(Integer, default=0)


class Topic(Base):
	"""
	topic model
	"""

	__tablename__ = 'topic'

	id = Column(Integer, primary_key=True)
	title = Column(String(20))
	content = Column(Text)

	def __init__(self, name):
		self.title = title

	def __repr__(self):
		return "<topic('%s','%s')>" %(self.id, self.title)


class TopicTag(Base):
	"""
	topic tag model
	"""

	__tablename__ = 'topic_tag'
	id = Column(Integer, primary_key=True)
	name = Column(String(20), default='')

	def __init__:
		pass		