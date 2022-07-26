from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src import config

SQLALCHEMY_DATABASE_URI = f"sqlite:///{str(config['SQLITE_FP'])}"
engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
