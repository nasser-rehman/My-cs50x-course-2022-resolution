import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def lookup(symbol):
    """Look up quote for symbol."""

    # Contact API
    try:
        api_key = os.environ.get("API_KEY")
        url = f"https://cloud.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/quote?token={api_key}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        quote = response.json()
        return {
            "name": quote["companyName"],
            "price": float(quote["latestPrice"]),
            "symbol": quote["symbol"]
        }
    except (KeyError, TypeError, ValueError):
        return None


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"


# Check if number is integer
def check_int(value):
    # Try to convert value
    try:
        # If value is instance of float return None
        if isinstance(value, float):
            return None
        # If value can be casted to int and higher than 0 return true
        if int(value) and int(value) > 0:
            return True
    # If error raise on casting, return None
    except ValueError:
        return None


# Check if number is float
def check_float(value):
    # Try to convert value
    try:
        # If value can be casted to float return true
        if float(value):
            return True
    # If error raise on casting, return None
    except ValueError:
        return None


# Replace , per .
def replacevalues(value):
    value = value.replace(',', '.', 1)
    return value


# Check if password provided by user is valid in requirements
def check_password_requirements(string):
    # Initialize variables
    check_lowercase = None
    check_uppercase = None
    check_digits = None
    check_punctuation = None

    # Loop through entire string
    for i in range(len(string)):
        # Check if character is lowercase
        if (string[i] in ascii_lowercase):
            # Set lowercase requirement True
            check_lowercase = True
        # Check if character is uppercase
        elif (string[i] in ascii_uppercase):
            # Set uppercase requirement True
            check_uppercase = True
        # Check if character is a digit
        elif (string[i] in digits):
            # Set digits requirement True
            check_digits = True
        # Check if character is punctuation
        elif (string[i] in punctuation):
            # Set punctuation requirement True
            check_punctuation = True

    # Check conditions and string length higher than 8
    if (check_lowercase and check_uppercase and check_digits and check_punctuation and len(string) >= 8):
        return True
    else:
        return None
