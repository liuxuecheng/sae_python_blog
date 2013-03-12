import sae.const
from sqlalchemy import create_engine

db_link = 'mysql+mysqldb://' + sae.const.MYSQL_USER + ':' + sae.const.MYSQL_PASS + '@' + sae.const.MYSQL_HOST + ':' + int(sae.const.MYSQL_PORT) + '/' + sae.const.MYSQL_DB

engine = create_engine(db_link)
