student = {}  # Make sure student dictionary exists

while True:
    try:
        choice = int(input("Enter the choice:\n 1=Store Details\n 2=Display Details\n 3=Update Details\n 4=Delete Details\n"))

        if choice == 1:
            student["name"] = input("Enter student Name: ")
            student["Roll_no"] = input("Enter the roll number: ")
            student["Course"] = input("Enter Course: ")
            student["Main_Subject"] = input("Enter Main Subject: ")

        elif choice == 2:
            if not student:
                print("No student details found. Please store details first!")
            else:
                print(student)

        elif choice == 3:
            if not student:
                print("No student details found. Please store details first!")
            else:
                field = input("Which field do you want to update? (name / Roll_no / Course / Main_Subject): ")
                if field in student:
                    student[field] = input(f"Enter new value for {field}: ")
                    print(f"{field} updated successfully")
                else:
                    print("Invalid field")

        elif choice == 4:
            if not student:
                print("No student details found. Please store details first!")
            else:
                student.clear()
                print("Student details deleted successfully")

        else:
            print("Invalid choice")

    except Exception as e:
        print("An error occurred:", e)