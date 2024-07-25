from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, Message  # Ensure the correct import

# Replace with your actual database URL
engine = create_engine('sqlite:///your_database.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def make_messages():
    messages = [
        {"body": "Hello, World!"},
        {"body": "This is a test message."},
        {"body": "Another message."}
    ]

    for msg in messages:
        message = Message(body=msg["body"])
        session.add(message)
    session.commit()

make_messages()
