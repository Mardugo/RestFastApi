# create_db.py

from models import metadata, engine

metadata.create_all(bind=engine)
