from db_settings import Base, engine, Session, Photos
import redis


def insert_to_postgres():
    Base.metadata.create_all(bind=engine)
    r = redis.Redis(host="localhost", port=63780, db=0)
    while True:
        size = r.rpop("photos")
        if size:
            size = len(size)
            with Session() as session:
                new = Photos(size=size)
                session.add(new)
                session.commit()
