
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Connect to SQLite database (creates file if not exists)
db = sqlite3.connect("database.db", check_same_thread=False)
cursor = db.cursor()

# Create tables if they don't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    password TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS student5 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT
)
''')

db.commit()


# -------- ROUTES --------

@app.route("/")
def home():
    return render_template("home.html")


# REGISTER
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        try:
            cursor.execute(
                "INSERT INTO users (name,email,password) VALUES (?,?,?)",
                (name, email, password)
            )
            db.commit()
            return "Registered Successfully"
        except sqlite3.IntegrityError:
            return "Email already exists!"

    return render_template("register.html")


# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        cursor.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password)
        )
        user = cursor.fetchone()

        if user:
            return redirect("/dashboard")
        else:
            return "Invalid Credentials"

    return render_template("login.html")


# DASHBOARD
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# STUDENTS
@app.route("/students", methods=["GET", "POST"])
def students():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        course = request.form["course"]

        cursor.execute(
            "INSERT INTO student5 (name, age, course) VALUES (?,?,?)",
            (name, age, course)
        )
        db.commit()

    cursor.execute("SELECT * FROM student5")
    data = cursor.fetchall()
    return render_template("student5.html", students=data)


# ITEMS
@app.route("/items", methods=["GET", "POST"])
def items():
    if request.method == "POST":
        title = request.form["title"]
        cursor.execute("INSERT INTO items (title) VALUES (?)", (title,))
        db.commit()

    cursor.execute("SELECT * FROM items")
    data = cursor.fetchall()
    return render_template("items.html", items=data)


# -------- RUN SERVER --------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)







# from flask import Flask, render_template, request,redirect
# import mysql.connector

# app = Flask(__name__)

# # database connection
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Ashwini",
#     database="flask_project"
# )

# cursor = db.cursor()

# @app.route("/")
# def home():
#     return '''
#     <h1>Home Page</h1>
#     <a href="/register">Register</a><br><br>
#     <a href="/login">Login</a>
#     '''

# # REGISTER
# @app.route("/register", methods=["GET","POST"])
# def register():
#     if request.method == "POST":
#         name = request.form["name"]
#         email = request.form["email"]
#         password = request.form["password"]

#         query = "INSERT INTO users (name,email,password) VALUES (%s,%s,%s)"
#         values = (name,email,password)

#         cursor.execute(query, values)
#         db.commit()

#         return "Registered Successfully"

#     return render_template("register.html")


# # LOGIN
# @app.route("/login", methods=["GET","POST"])
# def login():
#     if request.method == "POST":
#         email = request.form["email"]
#         password = request.form["password"]

#         query = "SELECT * FROM users WHERE email=%s AND password=%s"
#         values = (email,password)

#         cursor.execute(query, values)
#         user = cursor.fetchone()

#         if user:
#             return redirect("/dashboard")
#         else:
#             return "Invalid Credentials"

#     return render_template("login.html")


# @app.route("/dashboard")
# def dashboard():
#     return render_template("dashboard.html")


# @app.route("/students", methods=["GET","POST"])
# def students():
#     if request.method == "POST":
#         name = request.form["name"]
#         age = request.form["age"]
#         course = request.form["course"]

#         cursor.execute(
#             "INSERT INTO student5(name,age,course) VALUES(%s,%s,%s)",
#             (name,age,course)
#         )
#         db.commit()

#     cursor.execute("SELECT * FROM student5")
#     data = cursor.fetchall()

#     return render_template("student5.html", students=data)

# @app.route("/items", methods=["GET","POST"])
# def items():
#     if request.method == "POST":
#         title = request.form["title"]
#         cursor.execute("INSERT INTO items(title) VALUES(%s)", (title,))
#         db.commit()

#     cursor.execute("SELECT * FROM items")
#     data = cursor.fetchall()

#     return render_template("items.html", items=data)
# # if __name__=="__main__":
# #     app.run(debug=True)
# if __name__=="__main__": 
#     app.run(host="0.0.0.0",port=10000)











