import atexit
from sqlalchemy import Column, Integer, DateTime, create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

PG_DSN = "postgresql://user:1234@127.0.0.1:5431/photos"
engine = create_engine(PG_DSN)
Base = declarative_base()
Session = sessionmaker(bind=engine)
atexit.register(engine.dispose)


class Photos(Base):

    __tablename__ = "photos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    time = Column(DateTime, server_default=func.now())
    size = Column(Integer)
