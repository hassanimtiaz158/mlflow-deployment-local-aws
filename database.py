from sqlalchemy import create_engine
import os

os.makedirs("data", exist_ok=True)
engine = create_engine("sqlite:///data/mydb.db")
