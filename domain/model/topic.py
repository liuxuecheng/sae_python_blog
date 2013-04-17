# -*- coding: utf-8 -*-
from domain.model import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey


class Category(Base):
	"""
	Category model
	"""
	__tablename__ = 'topic_category'
	id = Column(Integer, primary_key=True)
	name = Column(String(20), default='')

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return "<topoc_category('%s')>" %(self.name, self.name)	


class Topic(Base):
	"""
	topic model
	"""

	__tablename__ = 'topic'

	id = Column(Integer, primary_key=True)
	title = Column(String(20))
	content = Column(Text)
	category_id = Column(Integer, ForeignKey('category.id'))
	priority = Column(Integer, default=0)

	category = relationship("Category", backref=backref('topic', order_by=id))

	def __init__(self, title):
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

	def __init__(self):
		pass		