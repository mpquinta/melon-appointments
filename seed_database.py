"""Script to seed database"""

import os
from datetime import datetime

import model
import crud
import server

os.system('dropdb melon-appts')
os.system('createdb melon-appts')

model.connect_to_db(server.app)
model.db.create_all()

users_in_db = []
for i in range(5):
    username = f'user{i}'
    new_user = crud.create_user(username)
    users_in_db.append(new_user)

model.db.session.add_all(users_in_db)
model.db.session.commit()
