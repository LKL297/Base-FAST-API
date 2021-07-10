from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import Config
from urllib import parse
import pyodbc


drivers = [item for item in pyodbc.drivers()]
driver = drivers[-1]

SQLALCHEMY_DATABASE_URL = "mssql+pyodbc://%s:%s@%s/%s?driver=%s" % (Config.DB_USER,Config.DB_PASSWORD,Config.DB_HOST,Config.DB,driver)


engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

SessionLocal.configure(bind=engine)
    

Base = declarative_base()
Base.metadata.bind = engine
Base.metadata.create_all(engine)
