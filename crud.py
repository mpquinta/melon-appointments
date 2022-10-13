"""CRUD Operations"""

import os
import json
from model import db, User, Appointment, connect_to_db

def create_user(username):
    new_user = User(username=username)
    return new_user

def username_already_exists(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return user
    return False

def get_unavailable_appts(scheduled_date, start_time, end_time):
    available_appts = Appointment.query.filter(
                        Appointment.scheduled_date == scheduled_date,
                        Appointment.start_time >= start_time,
                        Appointment.end_time <= end_time
                    ).all()
    return available_appts

def create_appt(user_id, scheduled_date, start_time, end_time):
    appt = Appointment(
            user_id=user_id, 
            scheduled_date=scheduled_date, 
            start_time=start_time, 
            end_time=end_time)
    return appt
