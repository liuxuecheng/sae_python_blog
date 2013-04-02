import sae.const
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from domain.model import Base

db_link = 'mysql+mysqldb://' + sae.const.MYSQL_USER + ':' + sae.const.MYSQL_PASS + '@' + sae.const.MYSQL_HOST + ':' + sae.const.MYSQL_PORT + '/' + sae.const.MYSQL_DB

engine = create_engine(db_link)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base.query = db_session.query_property()