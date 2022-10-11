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