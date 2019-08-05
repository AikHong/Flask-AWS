# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)

import sqlalchemy as db

#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://GCS:GCS368001@gymdb.cfcjymcgcyn5.ap-southeast-1.rds.amazonaws.com:3306/gymdb'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://AikHong:password1234@gym2.cfcjymcgcyn5.ap-southeast-1.rds.amazonaws.com:3306/GreatDB'
#engine = db.create_engine('mysql+pymysql://GCS:GCS368001@gymdb.cfcjymcgcyn5.ap-southeast-1.rds.amazonaws.com:3306/gymdb')
#connection = engine.connect()


# Uncomment the line below if you want to work with a local DB
#SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True
SECRET_KEY = 'U7OApAEgWuML1BAZGhL0FUoNydPqFkPhZlDHZXyv'
