from sqlalchemy.ext.declarative import declarative_base, declared_attr

class _Base(object):
    """
    Custom base model.
    """

    @classmethod
    def get(cls, id):
        """
        Get object by it's id.
        """

        return cls.query.get(id)

    @classmethod
    def gets(cls, ids):
        """
        Get objects by id list.
        """

        ids = {}.fromkeys(ids).keys()
        if len(ids) > 0:
            return cls.query.filter(cls.id.in_(ids))
        else:
            return []

    @declared_attr
    def __tablename__(cls):
        """
        Automatic cover model map tablename to lower
        """

        return cls.__name__.lower()

    # Default table config.
    __table_args__ = {'mysql_charset': 'utf8',
                      'mysql_engine': ''}


Base = declarative_base(cls=_Base)