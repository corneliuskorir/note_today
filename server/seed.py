from random import randint, choice as rc

from faker import Faker

from . import create_app
from .config import db
from .models import *

faker = Faker()

app = create_app()

with app.app_context():
    print("Deleting Records...")
    User.query.delete()
    Entry.query.delete()

    fake = Faker()

    print("Creating users...")

    users = []
    usernames = []

    for i in range(5):

        username = fake.first_name()
        while username in usernames:
            username = fake.first_name()
        usernames.append(username)

        user = User(username=username)
        user.password_hash = user.username

        users.append(user)

    db.session.add_all(users)

    print("Creating journal entries..")

    entries = []

    for i in range(100):
        content = fake.paragraph(nb_sentences=10)

        entry = Entry(title=fake.sentence(), content=content)

        entry.user = rc(users)

        entries.append(entry)

    db.session.add_all(entries)

    db.session.commit()
    print("Complete")
