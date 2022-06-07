from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
SQL_DATABASEURL='postgresql://postgres:patil123@localhost:5432/ECOMM'
engine=create_engine(SQL_DATABASEURL)

Sessionlocal=sessionmaker(bind=engine,autocommit=False,autoflush=False)

base=declarative_base()

