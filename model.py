"""Models for Melon Tasting Scheduling app"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """A user"""

    __tablename__ = "users"

    username = db.Column(db.String, nullable=False, unique=True)

    def __repr__(self):
        return f'<username: {self.username}>'

class Appointment(db.Model):
    """Saved appointments"""

    __tablename__ = "appointments"

    scheduled_date = db.Column(db.Datetime)
    user = db.relationship("User", backref="appointments")

    def __repr__(self):
        return f'<appointment={self.scheduled_date}>'

def connect_to_db(flask_app, db_uri="postgresql:///melon-appts", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)