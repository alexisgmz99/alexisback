from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_-w85Zyjpr_EOru5Z--G@test-utxicotepec-bd.h.aivencloud.com:21541/defaultdb"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
