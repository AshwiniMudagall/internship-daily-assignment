import mysql.connector;#This is required to connect our python to the mysql database
conn=mysql.connector.connect(host="localhost",user="root",password="Ashwini", database="studentdetail")
cursor=conn.cursor()
cursor.execute("select database()")
print("connected to database:",cursor.fetchone())

cursor.execute("select  distinct * from studentinfo")
for row in cursor.fetchall():
    print(row)

#To retrieve values from student table
cursor.execute("select distinct name,course from studentinfo")
for row in cursor.fetchall():
 print(row[0],row[1])

cursor.execute("""insert into studentinfo(name,reg_no,Course,College_name,major_subject,DOB) values ('manohar','435','Engineering','JSS college','Computer Science','2000-09-18')""")
conn.commit() 
print("Successfully added") 


#To delete a row
cursor.execute("delete from studentinfo where name='Ashwini'")
cursor.execute("select * from studentinfo")
for row in cursor.fetchall():
    print(row)

conn.commit()
print("Succesfully deleted")

#To delete duplicates
cursor.execute("select distinct * from studentinfo")
for row in cursor.fetchall():
        print(row[0],row[1])

#Updating manohar register number
cursor.execute("update studentinfo set reg_no='89' where name='manohar'")   
conn.commit()
print("succesfully updated")     

print("After Updation")
cursor.execute("select  distinct * from studentinfo")
for row in cursor.fetchall():
    print(row)


cursor.close()
conn.close()
