from sqlalchemy import create_engine # Engine banane ke liye
from sqlalchemy.ext.declarative import declarative_base # Tables banane ke liye base
from sqlalchemy.orm import sessionmaker # Database se baat karne ke liye session

# 1. Database ka Address (SQLite file banayega 'stocks.db')
SQLALCHEMY_DATABASE_URL = "sqlite:///./stocks.db"

# 2. Engine create karna (Connection point)
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# 3. Session taiyar karna (Query bhejne ke liye)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Base class (Isse hum apne Tables banayenge)
Base = declarative_base()