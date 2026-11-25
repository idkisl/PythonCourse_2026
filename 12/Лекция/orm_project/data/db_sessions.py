from sqlalchemy import create_engine, event
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///studio_people.db')

# SQLite проверяет внешние ключи для каждого соединения.
@event.listens_for(engine, 'connect')
def enable_foreign_keys(connection, record):
    connection.execute('PRAGMA foreign_keys = ON')

Session = sessionmaker(bind=engine)
