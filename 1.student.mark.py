students = []
courses = []
marks = {}

# Input functions
def input_student_infor(num_students):
    for i in range(num_students):
        student_id = input("Student ID: ")
        name = input("Student name: ")
        dob = input("Date of birth: ")
        students.append({"id": student_id, "name": name, "dob": dob})

def input_course_infor(num_courses):
    for _ in range(num_courses):
        course_id = input("Course ID: ")
        name = input("Course name: ")
        courses.append({"id": course_id, "name": name})

def input_marks_for_course():
    course_id = input("Course ID to input marks: ")
    if course_id not in [course["id"] for course in courses]:
        print("Course ID not found!")
        return
    
    for student in students:
        student_id = student["id"]
        mark = float(input(f"Mark for student {student['name']} (ID: {student_id}): "))
        if course_id not in marks:
            marks[course_id] = {}
        marks[course_id][student_id] = mark

# List functions
def list_courses():
    print("\nList of courses:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")

def list_students():
    print("\nList of students:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")

def show_marks_for_course():
    course_id = input("Enter course ID: ")
    if course_id not in marks:
        print("No marks")
        return
    
    print(f"\nMarks for course ID {course_id}:")
    for student_id, mark in marks[course_id].items():
        student = next((s for s in students if s["id"] == student_id), None)
        if student:
            print(f"Student: {student['name']} (ID: {student_id}), Mark: {mark}")
        else:
            print(f"Unknown student with ID {student_id}, Mark: {mark}")
  
# Main
while True:
    num_students = int(input("Number of student: "))
    if num_students <= 0:
        print("Invalid number, please try again")
    else:
        break

input_student_infor(num_students)

while True:
    num_courses = int(input("Number of course: "))
    if num_courses <= 0:
        print("Invalid number, please try again")
    else:
        break
    
input_course_infor(num_courses)
    
while True:
    print("1. Input marks for a course")
    print("2. List all courses")
    print("3. List all students")
    print("4. Show marks for a course")
    print("5. Exit")
        
    choice = int(input("Enter your choice: "))
    if choice == 1:
        input_marks_for_course()
    elif choice == 2:
        list_courses()
    elif choice == 3:
        list_students()
    elif choice == 4:
        show_marks_for_course()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
