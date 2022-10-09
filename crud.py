"""CRUD Operations"""

import os
import json
from model import db, User, Appointment, connect_to_db

def create_user(username):
    new_user = User(username=username)
    return new_user

def username_already_exists(username):
    if User.query.filter_by(username=username).all():
        return True
    return False