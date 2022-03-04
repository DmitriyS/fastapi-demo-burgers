from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from cafe.config import settings


engine = create_engine(settings.sqlalchemy_url, connect_args={'check_same_thread': False})
session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = session_factory()
