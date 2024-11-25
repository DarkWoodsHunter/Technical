from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#Define destiny of the database. This should be in a .env file
URL_DATABASE = 'sqlite:/// dbA.db'
#"mysql+pymysql://root:e15462813@localhost:3306/technicaltest"
engine = create_engine(URL_DATABASE, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()