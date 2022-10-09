"""Server for Melon Tasting Scheduling app"""

from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined
from datetime import datetime

# creates a server
app = Flask(__name__)
app.secret_key = "rabbits"
# Not sure what this does lol
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def homepage():
    """Website's homepage - user can login here"""
    
    return render_template("homepage.html")

@app.route("/login")
def login():
    """Verifies if user already has an account with the website"""

    # call crud operation to verify if the username is in the table
    # if not, add it to the database
    # add current user_id to session

    pass

@app.route("/logout")
def logout():
     """Logs a user out"""

    # delete session 
    
     pass

@app.route("/search-appts")
def search_appts():
    """Displays a page where users can select a date and time to see available appointmets"""

    # return render_template for HTML page with form
    pass

@app.route("/results")
def results():
    """Show results from searching available appointments"""

    # crud operation that returns all times that are not saved in the db already
    # make sure appointment times are 30 minutes long

    pass

@app.route("/save-appt", methods=["POST"])
def save_appt():
    """User can save appointment"""

    # get values from form
    # make sure user doesn't already have an appointment for a given day
    # if everything checks out, call crud function to create a appointment for given user
        # how to associate username to user_id?
    # else, display an error message using flash 
    # add to db
    # commit
    
    pass

@app.route("/schedule")
def schedule():
    """Show all of a user's scheduled appointments"""

    # crud function that queries all appointments for a given user_id
    # return results

    pass



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)