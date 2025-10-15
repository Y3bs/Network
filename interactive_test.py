#!/usr/bin/env python3
"""
Interactive test script for University Management System
Use this to manually test specific features
"""

from University import University, Student, Course

def interactive_menu():
    """Interactive menu for testing"""
    university = University()
    
    while True:
        print("\n" + "=" * 50)
        print("UNIVERSITY MANAGEMENT SYSTEM - INTERACTIVE TEST")
        print("=" * 50)
        print("1. Add Student")
        print("2. Add Course")
        print("3. Enroll Student in Course")
        print("4. Display All Data")
        print("5. Generate Report")
        print("6. Test Error Handling")
        print("7. Quick Demo (Add sample data)")
        print("8. Exit")
        
        choice = input("\nEnter your choice (1-8): ").strip()
        
        if choice == "1":
            add_student_interactive(university)
        elif choice == "2":
            add_course_interactive(university)
        elif choice == "3":
            enroll_student_interactive(university)
        elif choice == "4":
            university.display_data()
        elif choice == "5":
            university.report()
        elif choice == "6":
            test_errors_interactive()
        elif choice == "7":
            quick_demo(university)
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_student_interactive(university):
    """Interactive student creation"""
    print("\n--- Adding Student ---")
    try:
        student = Student()
        
        first_name = input("Enter first name: ").strip()
        student.set_first_name(first_name)
        
        last_name = input("Enter last name: ").strip()
        student.set_last_name(last_name)
        
        age = int(input("Enter age: "))
        student.set_age(age)
        
        gender = input("Enter gender (male/female): ").strip()
        student.set_gender(gender)
        
        university.add_student(student)
        print(f"✅ Student {first_name} {last_name} added successfully!")
        print(f"Student ID: {student.get_id()}")
        
    except ValueError as e:
        print(f"❌ Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

def add_course_interactive(university):
    """Interactive course creation"""
    print("\n--- Adding Course ---")
    try:
        course = Course()
        
        name = input("Enter course name: ").strip()
        course.set_course_name(name)
        
        university.add_course(course)
        print(f"✅ Course '{name}' added successfully!")
        print(f"Course Code: {course.get_course_code()}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def enroll_student_interactive(university):
    """Interactive enrollment"""
    print("\n--- Enrolling Student in Course ---")
    
    # Show available students
    students = university._University__students
    if not students:
        print("❌ No students available. Add students first.")
        return
    
    print("Available students:")
    for i, student in enumerate(students):
        print(f"{i+1}. {student.get_first_name()} {student.get_last_name()} (ID: {student.get_id()})")
    
    # Show available courses
    courses = university._University__courses
    if not courses:
        print("❌ No courses available. Add courses first.")
        return
    
    print("\nAvailable courses:")
    for i, course in enumerate(courses):
        print(f"{i+1}. {course.get_course_name()} (Code: {course.get_course_code()})")
    
    try:
        student_idx = int(input("\nEnter student number: ")) - 1
        course_idx = int(input("Enter course number: ")) - 1
        
        if 0 <= student_idx < len(students) and 0 <= course_idx < len(courses):
            courses[course_idx].enroll(students[student_idx])
            print(f"✅ {students[student_idx].get_first_name()} enrolled in {courses[course_idx].get_course_name()}")
        else:
            print("❌ Invalid selection.")
            
    except ValueError:
        print("❌ Please enter valid numbers.")
    except Exception as e:
        print(f"❌ Error: {e}")

def test_errors_interactive():
    """Interactive error testing"""
    print("\n--- Testing Error Handling ---")
    
    print("1. Testing invalid age...")
    try:
        student = Student()
        student.set_age(16)  # Should fail
    except ValueError as e:
        print(f"✅ Correctly caught: {e}")
    
    print("\n2. Testing empty name...")
    try:
        student = Student()
        student.set_first_name("")  # Should fail
    except ValueError as e:
        print(f"✅ Correctly caught: {e}")
    
    print("\n3. Testing invalid gender...")
    try:
        student = Student()
        student.set_gender("invalid")  # Should fail
    except ValueError as e:
        print(f"✅ Correctly caught: {e}")

def quick_demo(university):
    """Quick demo with sample data"""
    print("\n--- Quick Demo ---")
    
    # Add sample students
    sample_students = [
        {"first_name": "Ahmed", "last_name": "Hassan", "age": 20, "gender": "Male"},
        {"first_name": "Sara", "last_name": "Mahmoud", "age": 19, "gender": "Female"},
        {"first_name": "Omar", "last_name": "Youssef", "age": 22, "gender": "Male"},
    ]
    
    print("Adding sample students...")
    students = []
    for info in sample_students:
        student = Student()
        student.set_first_name(info["first_name"])
        student.set_last_name(info["last_name"])
        student.set_age(info["age"])
        student.set_gender(info["gender"])
        university.add_student(student)
        students.append(student)
        print(f"✅ {info['first_name']} {info['last_name']}")
    
    # Add sample courses
    sample_courses = [
        {"name": "Introduction to Programming"},
        {"name": "Data Structures"},
        {"name": "Database Systems"},
    ]
    
    print("\nAdding sample courses...")
    courses = []
    for info in sample_courses:
        course = Course()
        course.set_course_name(info["name"])
        university.add_course(course)
        courses.append(course)
        print(f"✅ {info['name']}")
    
    # Enroll students
    print("\nEnrolling students...")
    try:
        courses[0].enroll(students[0])  # Ahmed in Programming
        courses[1].enroll(students[1])  # Sara in Data Structures
        courses[2].enroll(students[2])  # Omar in Database Systems
        print("✅ Enrollments completed")
    except Exception as e:
        print(f"❌ Enrollment error: {e}")
    
    print("\nDemo completed! Use option 4 to view all data.")

if __name__ == "__main__":
    interactive_menu()
