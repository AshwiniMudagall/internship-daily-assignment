student_details={}#Creation of a empty dictionary

#Adding the elements
student_details["Name"]="Ashwini"
student_details["Register Number"]=461
student_details["USN"]="U02AS24S0461"
student_details["Course"]="BSc"
student_details["Core Subjects and marks Obtgained"]={"Physics":43,"Computer Science":100,"Mathematics":90

}#Nested Dictionary

student_details["Division"]="B1"
print(student_details)
print(type(student_details))

#Updating the elements of the dictionary

student_details["Name"]="Ammu"
student_details["USN"]="U02AS24S0679"
student_details["Course"]="Arts"

#Updation using method
student_details.update({"Register Number":90})
print("UPDATED VERSION:")
print(student_details)

print("Successfully created , added and updated the dictionary elements:")