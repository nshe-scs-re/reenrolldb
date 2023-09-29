from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import settings


# sqlite3
CONNECTION_STRING = settings.connection_string

# postgresql
# CONNECTION_STRING = "postgresql://{0}:{1}@{2}/{3}".format(settings.username,
#                                                          settings.password,
#                                                          settings.hostname,
#                                                          settings.database)

SQLALCHEMY_DATABASE_URL = CONNECTION_STRING

engine = create_engine(url=SQLALCHEMY_DATABASE_URL, echo=False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
