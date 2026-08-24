# Dictionary to store student records
# Key   -> Roll Number, Value -> Tuple containing (Name, Marks List)
students = {}

# Infinite loop - keeps showing the menu until user chooses Exit
while True:
    print("\n--- Student Record Manager ---")
    print("1. Add Student")
    print("2. Display Students with Average > 80")
    print("3. Update Student Marks")
    print("4. Display All Students of the college")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    # 1. ADD STUDENT
    if choice == 1:

        roll_no = int(input("Enter Roll Number: "))
        name = input("Enter Student Name: ")

        # Empty list to store marks of the student
        marks = []

        # Loop runs 3 times to accept 3 marks
        for i in range(3):
            mark = int(input("Enter Mark: "))

            # append() adds the mark to the marks list
            marks.append(mark)

        # Store data in the dictionary
        # roll_no is the dictionary KEY
        # (name, marks) is the dictionary VALUE
        # (name, marks) is a TUPLE
        students[roll_no] = (name, marks)

        print("Student record added successfully.")

    # 2. DISPLAY STUDENTS HAVING AVERAGE > 80
    elif choice == 2:

        print("\nStudents having average above 80:")

        # students.items() gives both:
        # dictionary key   -> roll_no
        # dictionary value -> student_data
        for roll_no, student_data in students.items():

            # student_data is a tuple:
            # student_data = (name, marks)

            # Index 0 contains the student name
            name = student_data[0]

            # Index 1 contains the marks list
            marks = student_data[1]

            total = 0

            # Add all marks one by one
            for mark in marks:
                total = total + mark

            # len(marks) gives the number of marks
            average = total / len(marks)

            # Display only students whose average is above 80
            if average > 80:
                print(roll_no, name, "Average =", average)

    # 3. UPDATE STUDENT MARKS
    elif choice == 3:

        roll_no = int(input("Enter Roll Number: "))

        # Check whether the roll number exists
        # as a key in the students dictionary
        if roll_no in students:

            # Get the existing student's name
            name = students[roll_no][0]

            # Create a new list for updated marks
            new_marks = []

            for i in range(3):
                mark = int(input("Enter New Mark: "))
                new_marks.append(mark)

            # Tuple is immutable, so instead of changing
            # the tuple directly, we create a new tuple
            # and replace the old dictionary value
            students[roll_no] = (name, new_marks)

            print("Marks updated successfully.")

        else:
            print("Student not found.")

    # 4. DISPLAY ALL STUDENTS
    elif choice == 4:

        print("\nStudent Records:")

        # Traverse all key-value pairs of the dictionary
        for roll_no, student_data in students.items():

            print(
                "Roll No:",
                roll_no,
                "Name:",
                student_data[0],      # Name from tuple
                "Marks:",
                student_data[1]       # Marks list from tuple
            )

    # 5. EXIT
    elif choice == 5:

        print("Program ended.")

        # break stops the while True loop
        break

    # Executed if user enters anything other than 1-5
    else:
        print("Invalid choice.")