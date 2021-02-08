from config import Config
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

ENGINE: Engine = create_engine(Config.DB_URL, pool_pre_ping=True)
SESSION: Session = sessionmaker(bind=ENGINE)()
