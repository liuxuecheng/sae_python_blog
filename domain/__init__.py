from sqlalchemy import create_engine 


engine = create_engine('mysql+mysqldb://' + SAE_MYSQL_USER + ':' + SAE_MYSQL_PASS + '@' + SAE_MYSQL_HOST_M + '/' + SAE_MYSQL_DB)

def get_version():
    return sqlalchemy.__version__
