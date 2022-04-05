import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # TODO: Add the user's entry into the database
        response = {'status': True, 'message': ''}

        if not request.form.get('name'):
            response['status'] = None
            response['message'] += "Name not provided. "

        if not request.form.get('month') or not int(request.form.get('month')) in range(1, 13, 1):
            response['status'] = None
            response['message'] += "Month not provided or invalid. "

        if not request.form.get('day') or not int(request.form.get('day')) in range(1, 32, 1):
            response['status'] = None
            response['message'] += "Day not provided or invalid. "

        if response['status'] == True:
            response['message'] = "Birthday successfully added"
            db.execute("INSERT INTO birthdays (name, month, day) VALUES (:name, :month, :day)", name=request.form.get(
                'name'), month=int(request.form.get('month')), day=int(request.form.get('day')))

        rows = db.execute('SELECT * FROM birthdays')
        return render_template('index.html', rows=rows, response=response)

    else:

        # TODO: Display the entries in the database on index.html

        # Select all birthdays from DB
        rows = db.execute('SELECT * FROM birthdays')
        response = {}
        response['status'] = True
        return render_template("index.html", rows=rows, response=response)