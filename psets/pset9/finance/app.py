import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd, check_password_requirements, replacevalues, check_int, check_float

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # Get all stocks that user bought
    wallet = db.execute(
        "SELECT * FROM wallet WHERE fk_user_id = :id", id=session["user_id"])
    # Get cash from user logged in
    user = db.execute("SELECT cash FROM users WHERE id = :id",
                      id=session["user_id"])
    # Used to get the total of stocks and cash of user
    total_active = 0

    # Iterate over all stocks and to get the actual price and data from every stocks that user have
    for row in range(len(wallet)):
        wallet[row]['name'] = lookup(wallet[row]['symbol'])['name']
        wallet[row]['price'] = usd(lookup(wallet[row]['symbol'])['price'])
        wallet[row]['total'] = usd(lookup(wallet[row]['symbol'])[
                                   'price'] * wallet[row]['quantity'])
        total_active += lookup(wallet[row]['symbol']
                               )['price'] * wallet[row]['quantity']

    # Sum cash from user to total of stocks values
    total_active += user[0]['cash']
    # Convert cash to USD value
    user[0]['cash'] = usd(user[0]['cash'])

    # Convert total active to USD value
    total_active = usd(total_active)
    # Return page with params to show user
    return render_template("index.html", wallet=wallet, user=user[0], total_active=total_active)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # Check if the request method is GET or POST
    if request.method == "GET":
        return render_template("buy.html")
    elif request.method == "POST":
        # Fetch all data from API with symbol provided by user
        search = lookup(request.form.get("symbol"))

        # Verify if the symbol provided from user is not empty or doesn't exist
        if not request.form.get("symbol") or search == None:
            return apology("must provide a valid symbol", 400)

        # Check if number provided for quantity shares can be cast to integer
        if not check_int(request.form.get("shares")):
            return apology("must provide a valid share quantity", 400)

        shares_quantity = int(request.form.get("shares"))

        # Get user data logged in
        user_data = db.execute(
            "SELECT * FROM users WHERE id = ?", session['user_id'])

        # Calculate the total price of value of stock and quantity that user wants
        total_price = search['price'] * shares_quantity

        # Calculate the ammount of cash that lasts to user after purchase
        user_new_cash = user_data[0]['cash'] - total_price

        # Check if ammount of chash is minor than 0, if yes return that user can't afford the purchase
        if user_new_cash < 0.00:
            return apology("Can't afford", 400)

        # Get data from wallet where the symbol is equals that he is trying to purchase if exists
        before_table = db.execute(
            "SELECT * FROM wallet WHERE symbol = ?", request.form.get("symbol"))

        # If exists on wallet, get the quantity of stocks that user already have in wallet of stock
        if before_table:
            shares_quantity += before_table[0]['quantity']

        # Insert new or replace if exists the new wallet quantity of stock
        db.execute("INSERT OR REPLACE INTO wallet (symbol, quantity, fk_user_id) VALUES (?, ?, ?) ",
                   search['symbol'], shares_quantity, user_data[0]['id'])

        # Insert into history log of purchase
        db.execute("INSERT INTO history (symbol, operation, quantity, price_operation, fk_user_id) VALUES (?, ?, ?, ?, ?) ",
                   search['symbol'], 'purchase', request.form.get('shares'), search['price'], user_data[0]['id'])

        # Update cash available to user that is purchasing the stocks
        db.execute("UPDATE users SET cash = ? WHERE id = ?",
                   user_new_cash, user_data[0]['id'])
        # Redirects to index
        return redirect('/')


@app.route("/history")
@login_required
def history():
    # Query all data from history of user logged in
    history = db.execute(
        "SELECT * FROM history WHERE fk_user_id = :user_id", user_id=session['user_id'])
    return render_template('history.html', history=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    # return apology("TODO")

    if request.method == "GET":
        return render_template("quote.html")
    elif request.method == "POST":
        if not request.form.get("symbol"):
            return apology("must provide a symbol", 400)

        quote = lookup(request.form.get("symbol"))
        if not quote:
            return apology("Must provide a valid symbol", 400)
        else:
            return render_template("quote.html", name=quote['name'], symbol=quote['symbol'], price=usd(quote['price']))


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Check if method of request is POST
    if request.method == "POST":
        # Verify if username was provided on form
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Verify if password was provided on form
        if not request.form.get("password"):
            return apology("must provide password", 400)

        # Verify if confirmation of password was provided on form
        if not request.form.get("confirmation"):
            return apology("must confirm provided password", 400)

        # Verify if the fields of password provided matches
        if request.form.get("password") != request.form.get("confirmation"):
            return apology("the passwords don't match", 400)

        if not check_password_requirements(request.form.get("password")):
            return apology("the password needs to be more strong", 400)

        # Select on DB to verify if already have a user with same username
        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          request.form.get("username"))

        # Check if select has element from query executed
        if len(rows) >= 1:
            return apology("username aready in use", 400)
        else:
            # If query doesn't find a username then insert the new one
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", request.form.get(
                "username"), generate_password_hash(request.form.get('password')))

        return redirect("/login")
    else:
        # If method is GET return the form register page
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        # Select to get all symbols of shares that user had
        wallet = db.execute(
            "SELECT symbol FROM wallet WHERE fk_user_id = :user_id", user_id=session["user_id"])
        return render_template("sell.html", wallet=wallet)
    elif request.method == "POST":
        # Check if symbol or share was provided by user
        if not request.form.get("symbol") or not request.form.get("shares"):
            return apology("must provide symbol and shares", 403)

        # Fetch data from wallet by symbol that user provided
        wallet = db.execute("SELECT * FROM wallet WHERE fk_user_id = :user_id AND symbol = :symbol",
                            user_id=session["user_id"], symbol=request.form.get('symbol'))

        # Return if symbol was not found
        if not wallet:
            return apology("Symbol not provided", 400)

        #  Check if shares provided by user is integer and not a float or string
        #  Return if isn't int
        if not check_int(request.form.get("shares")):
            return apology("Shares must be an integer value", 400)

        # Check if the quantity of shares provided by user is higher than that he already have
        # If higher, break
        if wallet[0]['quantity'] < int(request.form.get("shares")):
            return apology("Shares to sell higher than wallet", 400)

        # Collect user cash
        user_data = db.execute(
            "SELECT cash FROM users WHERE id = :id_user", id_user=session['user_id'])

        # Check the quantity that will be left after operation
        # If equals 0 then delete record from db if isn't update table
        if wallet[0]['quantity'] - int(request.form.get('shares')) == 0:
            db.execute("DELETE FROM wallet WHERE fk_user_id = :user_id AND symbol = :symbol",
                       user_id=session['user_id'], symbol=request.form.get('symbol'))
        else:
            db.execute("UPDATE wallet SET quantity = :quantity WHERE symbol = :symbol",
                       quantity=wallet[0]['quantity']-int(request.form.get('shares')), symbol=request.form.get('symbol'))

        # Insert on history table the operation
        db.execute("INSERT INTO history (symbol, operation, quantity, price_operation, fk_user_id) VALUES (?, ?, ?, ?, ?)",
                   wallet[0]['symbol'], "sell", request.form.get('shares'), lookup(request.form.get('symbol'))['price'], session["user_id"])

        # Update user cash after operation
        db.execute("UPDATE users SET cash = :cash WHERE id = :user_id", cash=user_data[0]['cash']+(lookup(
            request.form.get('symbol'))['price']*int(request.form.get('shares'))), user_id=session["user_id"])
    # Redirect to index
    return redirect("/")


@app.route("/addcash", methods=["POST"])
@login_required
def addcash():
    if request.method == 'POST':
        # Check if cash was provided by user
        if not request.form.get('cash'):
            return apology('cash must be provided', 403)
        # Check if value provided by user is an float value
        if not check_float(replacevalues(request.form.get('cash'))):
            return apology('cash must be a float value', 400)

        # Execute update on user
        db.execute('UPDATE users SET cash = cash + :cash WHERE id = :user_id',
                   cash=float(replacevalues(request.form.get('cash'))), user_id=session['user_id'])

    return redirect('/')


@app.route("/changepassword", methods=["GET", "POST"])
@login_required
def changepassword():
    if request.method == "GET":
        return render_template("changepassword.html")
    elif request.method == "POST":
        # Check if all form inputs were provided
        if not request.form.get("current_password"):
            return apology('current password must be provided', 400)

        if not request.form.get("new_password"):
            return apology('new password must be provided', 400)

        if not request.form.get("new_password_confirmation"):
            return apology('Confirmation of new password must be provided', 400)

        # Check if password is on requirements
        if not check_password_requirements(request.form.get('new_password')):
            return apology('password needs to be stronger', 400)

        # Check if input of new password match with confirmation of new password
        if request.form.get('new_password') != request.form.get('new_password_confirmation'):
            return apology('new password not match with confirmation', 400)

        # Get hash from user logged in
        rows_user = db.execute(
            "SELECT hash FROM users WHERE id = :user_id", user_id=session['user_id'])

        # Check if password provided by user is equals that are in database
        if len(rows_user) != 0 and not check_password_hash(rows_user[0]['hash'], request.form.get('current_password')):
            return apology('current password provided not valid', 400)

        # Execute update on user data hash fild
        db.execute('UPDATE users SET hash = :hash WHERE id=:user_id', hash=generate_password_hash(
            request.form.get('new_password')), user_id=session['user_id'])

        return redirect('/')
