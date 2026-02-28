from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Connecting  to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ashwini",  
    database="LoginDetails")            

cursor = db.cursor()

@app.route("/")
def login_page():
    return render_template("form2.html") 

@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"].strip()
    phone = request.form["phonenumber"].strip()

    query = "SELECT * FROM userinfo WHERE email=%s AND phonenumber=%s"
    cursor.execute(query, (email,phone))
    user = cursor.fetchone()

    if user:
        return redirect("/dashboard")
    else:
        return render_template("form2.html", error="Invalid Email or Phone")

@app.route("/dashboard")
def dashboard():
    return "<h2>Login Successful! Welcome 🎉</h2>"

if __name__ == "__main__":
    app.run(debug=True)