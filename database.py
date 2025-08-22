from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Imagine this as our "diary" where we write everything
DATABASE_URL = "sqlite:///./skillswap.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = the paper template for our diary
Base = declarative_base()

