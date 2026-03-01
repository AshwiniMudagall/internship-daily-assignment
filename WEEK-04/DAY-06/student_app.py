from flask import Flask,render_template,request,redirect 
import mysql.connector
app=Flask(__name__)

#Connecting to app_Database that i created for this program

conn=mysql.connector.connect(
host="localhost",
user="root",
password="Ashwini",database="app")
cursor=conn.cursor()




@app.route("/")
def home():
  return render_template("add.html")




#@app.route("/")
#def index():
# cursor.execute("select * from students3") 
 #data=cursor.fetchall()
 #return str(data) 

@app.route('/view')
def view():
   conn=mysql.connector.connect(
      host="localhost",
      user="root",
      password="Ashwini",
      database="app"    
          )
   cursor=conn.cursor(dictionary=True)
   cursor.execute("select * from students3")
   students=cursor.fetchall()

   return render_template("view.html",students=students)


@app.route("/add",methods=["POST"])
def add():
 
  name=request.form["name"]
  email=request.form["email"]
  reg_number=request.form["reg_number"]
  course=request.form["course"]
  sql="INSERT INTO STUDENTS3(name,reg_number,email,course) values (%s,%s,%s,%s)"
  values=(name,reg_number,email,course)

  cursor.execute(sql,values)
  conn.commit()

  return redirect("/students")

@app.route("/students")
def view_students():
  conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ashwini",
    database="app"
  )
  cursor=conn.cursor(dictionary=True)
  cursor.execute("select * from students3")
  data=cursor.fetchall()
  conn.close()
  return render_template("view.html",students=data)

  


@app.route("/delete/<reg>")
def delete(reg):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ashwini",
        database="app"
    )
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students3 WHERE reg_number=%s", (reg,))
    conn.commit()
    conn.close()

    return redirect("/students")
   
   
@app.route("/update/<reg_number>", methods=["POST"])
def update(reg_number):
    name = request.form["name"]
    email = request.form["email"]
    course = request.form["course"]
    new_reg = request.form["reg_number"]

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ashwini",
        database="app"
    )
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE students3 
        SET name=%s, reg_number=%s, email=%s, course=%s
        WHERE reg_number=%s
    """, (name, new_reg, email, course, reg_number))
    conn.commit()
    conn.close()

    return redirect("/students")




if __name__== "__main__":
    app.run(debug=True)


 
