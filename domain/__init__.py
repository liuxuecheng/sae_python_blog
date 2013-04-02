import sae.const
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_link = 'mysql+mysqldb://' + sae.const.MYSQL_USER + ':' + sae.const.MYSQL_PASS + '@' + sae.const.MYSQL_HOST + ':' + sae.const.MYSQL_PORT + '/' + sae.const.MYSQL_DB

engine = create_engine(db_link)
Session = sessionmaker(bind=engine)
db_session = Session()
Base.query = db_session.query_property()