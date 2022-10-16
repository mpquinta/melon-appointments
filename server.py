"""Server for Melon Tasting Scheduling app"""

from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined
import datetime

# creates a server
app = Flask(__name__)
app.secret_key = "rabbits"
# Not sure what this does lol
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def homepage():
    """Website's homepage - user can login here"""
    
    return render_template("homepage.html")

@app.route("/login", methods=["POST"])
def login():
    """Verifies if user already has an account with the website"""

    username = request.form.get("username")
    # call crud operation to verify if the username is in the table
    user_validation = crud.username_already_exists(username)
    if user_validation:
        session["signed_in_user"] = user_validation.user_id
    # if not, add it to the database
    else:
        new_user = crud.create_user(username)
        db.session.add(new_user)
        db.session.commit()
        session["signed_in_user"] = new_user.user_id
    # add current user_id to session
    return redirect("/search-appts")


@app.route("/logout")
def logout():
    """Logs a user out"""

    # delete session 
    del session["signed_in_user"]

    return redirect("/")
     

@app.route("/search-appts")
def search_appts():
    """Displays a page where users can select a date and time to see available appointmets"""

    # return render_template for HTML page with form
    return render_template("appointments.html")

@app.route("/results")
def results():
    """Show results from searching available appointments"""

    
    # retrieving information from the form the user filled out
    requested_date = request.args.get("date")
    start_time_hour = request.args.get("start_time_hour")
    start_time_min = request.args.get("start_time_min")
    start_time_am_pm = request.args.get("start_time_am_pm")
    end_time_hour = request.args.get("end_time_hour")
    end_time_min = request.args.get("end_time_min")
    end_time_am_pm = request.args.get("end_time_am_pm")

    #converting string time into datetime object
    start_time = datetime.datetime.strptime((start_time_hour + ":" + start_time_min + start_time_am_pm), "%I:%M%p")
    end_time = datetime.datetime.strptime(end_time_hour + ":" + end_time_min + end_time_am_pm, "%I:%M%p")

    # TODO: edge case end time is earlier than start time
    
    # call crud operation that returns all times that are not saved in the db already
    unavail_appts = crud.get_unavailable_appts(requested_date, start_time.time(), end_time.time())
    # since returns a datetime object, iterate over result and only save start times of saved appointments
    unavail_start_times = set()
    for appts in unavail_appts:
        unavail_start_times.add(appts.start_time)
    available_appts = {}
    
    # create a variable that will act as a key for the dictionary so result is ordered when sent back to front end
    counter = 0
    current = start_time

    while current < end_time:
        if current.time() not in unavail_start_times:
            available_appts[counter] = {
                "scheduled_day": requested_date,
                "appt_start": current.time().strftime("%I:%M%p"),
                "appt_end": (current + datetime.timedelta(minutes=30)).time().strftime("%I:%M%p")
            }
            # available_appts[counter] = current.time().strftime("%I:%M%p")
            counter += 1
        current = current + datetime.timedelta(minutes=30)

    print("unavailable appts: ", unavail_appts)
    print("available appts: ", available_appts)

    return available_appts

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