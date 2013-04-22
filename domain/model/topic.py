# -*- coding: utf-8 -*-
from domain.model import Base, timestamp_mixin
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship, backref


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


@timestamp_mixin
class Topic(Base):
	"""
	topic model
	"""

	__tablename__ = 'topic'

	id = Column(Integer, primary_key=True)
	title = Column(String(80))
	content = Column(Text)
	category_id = Column(Integer, default=0)
	priority = Column(Integer, default=0)

	#one to one
	count = relationship('TopicCount', lazy=True, uselist=False, backref='topic')

	def __init__(self, title):
		self.title = title
		self.count = TopicCount()

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


class TopicCount(Base):
	"""
	topic count
	"""

	__tablename__ = 'topic_count'
	id = Column(Integer, primary_key=True)
	topic_id = Column(Integer, ForeignKey('topic.id'))
	views = Column(Integer)
	reply_num = Column(Integer)