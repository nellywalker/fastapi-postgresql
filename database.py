from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#SI FASTAPI a l'interieur docker
#DATABASE_URL = "postgresql://ratiaharivoav:root905H-F@db:5432/pg17"

#Si FASTAPI a l'exterieur docker
#DATABASE_URL = "postgresql://ratiaharivoav:root905H-F@localhost:5432/pg17"
#DATABASE_URL = "postgresql://ratiaharivoav:root905H-F@127.0.0.1:5432/pg17"
DATABASE_URL = "postgresql://ratiaharivoav:root905H-F@localhost:5433/pg17"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()