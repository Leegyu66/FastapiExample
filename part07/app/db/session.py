from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = "sqlite:///example.db" # 1

engine = create_engine( # 2
    SQLALCHEMY_DATABASE_URI,
    connect_args={"check_same_thread": False}, # 3
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # 4