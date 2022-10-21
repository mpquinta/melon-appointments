"""CRUD Operations"""

import os
import json
from model import db, User, Appointment, connect_to_db
import datetime

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

def convert_str_to_datetime(time):
    date_time = datetime.datetime.strptime(time, "%I:%M%p")
    return date_time

def convert_datestr_to_datetime(date):
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    return date

def add_30_min(date_time):
    """Takes datetime object, adds 30 minutes and returns the time in string format."""
    return (date_time + datetime.timedelta(minutes=30)).time().strftime("%I:%M%p")

def appt_for_day_exists(scheduled_date, signed_in_user):
    if Appointment.query.filter(Appointment.user_id == signed_in_user, Appointment.scheduled_date == scheduled_date).all():
        return True
    return False

def convert_date_formatted_str(date):
    return date.strftime("%b %d, %Y")

def convert_time_formatted_str(time):
    return time.strftime("%I:%M%p")

def users_appts(user_id):
    all_appts = Appointment.query.filter_by(user_id=user_id).all()
    return all_appts


