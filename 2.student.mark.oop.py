class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

class StudentMarkManagement:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    # Input functions
    def input_number_of_students(self):
        n = int(input("Enter the number of students: "))
        for _ in range(n):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter date of birth (DD/MM/YYYY): ")
            self.students.append(Student(student_id, name, dob))

    def input_number_of_courses(self):
        n = int(input("Enter the number of courses: "))
        for _ in range(n):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            self.courses.append(Course(course_id, name))

    def input_marks(self):
        course_id = input("Enter the course ID to input marks: ")
        if course_id not in self.marks:
            self.marks[course_id] = {}

        print("Input marks for the course: ", course_id)
        for student in self.students:
            mark = float(input(f"Enter marks for student {student.name} (ID: {student.student_id}): "))
            self.marks[course_id][student.student_id] = mark

    # Listing functions
    def list_courses(self):
        print("\nList of Courses:")
        for course in self.courses:
            print(f"ID: {course.course_id}, Name: {course.name}")

    def list_students(self):
        print("\nList of Students:")
        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.name}, DOB: {student.dob}")

    def show_marks(self):
        course_id = input("Enter the course ID to show marks: ")
        if course_id in self.marks:
            print(f"\nMarks for Course {course_id}:")
            for student in self.students:
                mark = self.marks[course_id].get(student.student_id, "N/A")
                print(f"Student {student.name} (ID: {student.student_id}): {mark}")
        else:
            print("No marks recorded for this course!")


system = StudentMarkManagement()
while True:
    print("\nStudent Mark Management System")
    print("1. Input number of students")
    print("2. Input student information")
    print("3. Input number of courses")
    print("4. Input course information")
    print("5. Input marks for a course")
    print("6. List courses")
    print("7. List students")
    print("8. Show student marks for a course")
    print("9. Exit")
        
    choice = input("Choose an option: ")
    if choice == "1":
        system.input_number_of_students()
    elif choice == "2":
        system.input_number_of_students()
    elif choice == "3":
        system.input_number_of_courses()
    elif choice == "4":
        system.input_number_of_courses()
    elif choice == "5":
        system.input_marks()
    elif choice == "6":
        system.list_courses()
    elif choice == "7":
        system.list_students()
    elif choice == "8":
        system.show_marks()
    elif choice == "9":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
