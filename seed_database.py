"""Script to seed database"""

import os
import datetime

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

appointments_in_db = []
for i in range(1, 6):
    new_appt = crud.create_appt(
                user_id=i, 
                scheduled_date=datetime.datetime.now().date().strftime("%m/%d/%Y"), 
                start_time=datetime.datetime.now().time().strftime("%I:%M%p"),
                end_time=(datetime.datetime.now() + datetime.timedelta(minutes=30)).time().strftime("%I:%M%p")
    )

    appointments_in_db.append(new_appt)
model.db.session.add_all(appointments_in_db)
model.db.session.commit()

