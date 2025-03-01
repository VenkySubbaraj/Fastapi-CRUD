from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import urllib.parse
from dotenv import load_dotenv

load_dotenv()
import os

password = os.getenv("password")
encrypted_password = urllib.parse.quote(password)
DB_url = f"mysql+pymysql://venkat:{encrypted_password}@localhost:3306/fast_api"
print(DB_url)
engine = create_engine(DB_url, echo=True)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
base = declarative_base()