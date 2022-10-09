"""CRUD Operations"""

import os
import json
from model import db, User, Appointment, connect_to_db

def create_user(username):
    new_user = User(username=username)
    return new_user