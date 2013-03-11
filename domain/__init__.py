import sae.const 
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqldb://' + sae.const.MYSQL_USER + ':' + sae.const.MYSQL_PASS + '@' + sae.const.MYSQL_HOST_M + '/' + sae.const.MYSQL_DB)

def get_version():
    return sqlalchemy.__version__