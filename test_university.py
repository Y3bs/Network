#!/usr/bin/env python3
"""
Test script for University Management System
This script tests all functionality including:
- Student creation and management
- Course creation and management
- Enrollment system
- Error handling
- Data display and reports
"""

from University import University, Student, Course

def test_student_creation():
    """Test creating students with valid data"""
    print("=" * 50)
    print("TESTING STUDENT CREATION")
    print("=" * 50)
    
    university = University()
    
    # Test data for students
    test_students = [
        {"first_name": "Ahmed", "last_name": "Hassan", "age": 20, "gender": "Male"},
        {"first_name": "Sara", "last_name": "Mahmoud", "age": 19, "gender": "Female"},
        {"first_name": "Omar", "last_name": "Youssef", "age": 22, "gender": "Male"},
        {"first_name": "Lina", "last_name": "Adel", "age": 21, "gender": "Female"},
        {"first_name": "Karim", "last_name": "Nabil", "age": 23, "gender": "Male"},
        {"first_name": "Mariam", "last_name": "Fathy", "age": 20, "gender": "Female"},
        {"first_name": "Youssef", "last_name": "Ali", "age": 24, "gender": "Male"},
        {"first_name": "Nour", "last_name": "Samir", "age": 19, "gender": "Female"},
        {"first_name": "Hossam", "last_name": "Tarek", "age": 22, "gender": "Male"},
        {"first_name": "Dalia", "last_name": "Magdy", "age": 21, "gender": "Female"},
    ]
    
    print("Creating students...")
    for i, info in enumerate(test_students, 1):
        try:
            student = Student()
            student.set_first_name(info["first_name"])
            student.set_last_name(info["last_name"])
            student.set_age(info["age"])
            student.set_gender(info["gender"])
            university.add_student(student)
            print(f"✅ Student {i}: {info['first_name']} {info['last_name']} added successfully")
        except Exception as e:
            print(f"❌ Student {i}: Error - {e}")
    
    return university

def test_course_creation():
    """Test creating courses"""
    print("\n" + "=" * 50)
    print("TESTING COURSE CREATION")
    print("=" * 50)
    
    university = University()
    
    # Test data for courses
    test_courses = [
        {"name": "Introduction to Programming"},
        {"name": "Data Structures and Algorithms"},
        {"name": "Database Systems"},
        {"name": "Computer Networks"},
        {"name": "Operating Systems"},
        {"name": "Artificial Intelligence"},
        {"name": "Web Development"},
        {"name": "Mobile App Development"},
        {"name": "Software Engineering"},
        {"name": "Machine Learning"},
        {"name": "Cybersecurity"},
        {"name": "Cloud Computing"},
    ]
    
    print("Creating courses...")
    for i, info in enumerate(test_courses, 1):
        try:
            course = Course()
            course.set_course_name(info["name"])
            university.add_course(course)
            print(f"✅ Course {i}: {info['name']} added successfully")
        except Exception as e:
            print(f"❌ Course {i}: Error - {e}")
    
    return university

def test_error_handling():
    """Test error handling scenarios"""
    print("\n" + "=" * 50)
    print("TESTING ERROR HANDLING")
    print("=" * 50)
    
    # Test invalid age
    print("Testing invalid age (under 18)...")
    try:
        student = Student()
        student.set_age(16)  # Should raise error
        print("❌ Error: Should have raised ValueError for age < 18")
    except ValueError as e:
        print(f"✅ Correctly caught error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    
    # Test empty name
    print("\nTesting empty first name...")
    try:
        student = Student()
        student.set_first_name("")  # Should raise error
        print("❌ Error: Should have raised ValueError for empty name")
    except ValueError as e:
        print(f"✅ Correctly caught error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    
    # Test invalid gender
    print("\nTesting invalid gender...")
    try:
        student = Student()
        student.set_gender("invalid")  # Should raise error
        print("❌ Error: Should have raised ValueError for invalid gender")
    except ValueError as e:
        print(f"✅ Correctly caught error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

def test_enrollment_system():
    """Test the enrollment system"""
    print("\n" + "=" * 50)
    print("TESTING ENROLLMENT SYSTEM")
    print("=" * 50)
    
    university = University()
    
    # Create some students
    students_data = [
        {"first_name": "Ahmed", "last_name": "Hassan", "age": 20, "gender": "Male"},
        {"first_name": "Sara", "last_name": "Mahmoud", "age": 19, "gender": "Female"},
        {"first_name": "Omar", "last_name": "Youssef", "age": 22, "gender": "Male"},
    ]
    
    students = []
    for info in students_data:
        student = Student()
        student.set_first_name(info["first_name"])
        student.set_last_name(info["last_name"])
        student.set_age(info["age"])
        student.set_gender(info["gender"])
        university.add_student(student)
        students.append(student)
    
    # Create some courses
    courses_data = [
        {"name": "Introduction to Programming"},
        {"name": "Data Structures"},
        {"name": "Database Systems"},
    ]
    
    courses = []
    for info in courses_data:
        course = Course()
        course.set_course_name(info["name"])
        university.add_course(course)
        courses.append(course)
    
    # Test enrollment
    print("Testing course enrollment...")
    try:
        # Enroll students in courses 
        for i, student in enumerate(students):
            for j, course in enumerate(courses):
                if i == j:  # Each student enrolls in one course
                    course.enroll(student)
                    print(f"✅ {student.get_first_name()} enrolled in {course.get_course_name()}")
    except Exception as e:
        print(f"❌ Enrollment error: {e}")

def test_full_system():
    """Test the complete system with all features"""
    print("\n" + "=" * 50)
    print("TESTING FULL SYSTEM")
    print("=" * 50)
    
    university = University()
    
    # Create students
    students_data = [
        {"first_name": "Ahmed", "last_name": "Hassan", "age": 20, "gender": "Male"},
        {"first_name": "Sara", "last_name": "Mahmoud", "age": 19, "gender": "Female"},
        {"first_name": "Omar", "last_name": "Youssef", "age": 22, "gender": "Male"},
        {"first_name": "Lina", "last_name": "Adel", "age": 21, "gender": "Female"},
        {"first_name": "Karim", "last_name": "Nabil", "age": 23, "gender": "Male"},
    ]
    
    print("Creating students...")
    students = []
    for info in students_data:
        student = Student()
        student.set_first_name(info["first_name"])
        student.set_last_name(info["last_name"])
        student.set_age(info["age"])
        student.set_gender(info["gender"])
        university.add_student(student)
        students.append(student)
        print(f"✅ {info['first_name']} {info['last_name']} (ID: {student.get_id()})")
    
    # Create courses
    courses_data = [
        {"name": "Introduction to Programming"},
        {"name": "Data Structures"},
        {"name": "Database Systems"},
        {"name": "Computer Networks"},
        {"name": "Operating Systems"},
    ]
    
    print("\nCreating courses...")
    courses = []
    for info in courses_data:
        course = Course()
        course.set_course_name(info["name"])
        university.add_course(course)
        courses.append(course)
        print(f"✅ {info['name']} (Code: {course.get_course_code()})")
    
    # Enroll students in courses
    print("\nEnrolling students in courses...")
    enrollments = [
        (0, 0),  # Ahmed in Programming
        (0, 1),  # Ahmed in Data Structures
        (1, 1),  # Sara in Data Structures
        (1, 2),  # Sara in Database Systems
        (2, 2),  # Omar in Database Systems
        (2, 3),  # Omar in Networks
        (3, 3),  # Lina in Networks
        (3, 4),  # Lina in Operating Systems
        (4, 4),  # Karim in Operating Systems
        (4, 0),  # Karim in Programming
    ]
    
    for student_idx, course_idx in enrollments:
        try:
            courses[course_idx].enroll(students[student_idx])
            print(f"✅ {students[student_idx].get_first_name()} enrolled in {courses[course_idx].get_course_name()}")
        except Exception as e:
            print(f"❌ Enrollment failed: {e}")
    
    # Display all data
    print("\n" + "=" * 50)
    print("DISPLAYING ALL DATA")
    print("=" * 50)
    university.display_data()
    
    # Generate report
    print("\n" + "=" * 50)
    print("GENERATING REPORT")
    print("=" * 50)
    university.report()
    
    return university

def main():
    """Run all tests"""
    print("UNIVERSITY MANAGEMENT SYSTEM - COMPREHENSIVE TEST")
    print("=" * 60)
    
    # Run individual tests
    test_student_creation()
    test_course_creation()
    test_error_handling()
    test_enrollment_system()
    
    # Run full system test
    university = test_full_system()
    
    print("\n" + "=" * 60)
    print("ALL TESTS COMPLETED!")
    print("=" * 60)
    
    # Final statistics
    print(f"\nFinal Statistics:")
    print(f"Total Students: {len(university._University__students)}")
    print(f"Total Courses: {len(university._University__courses)}")

if __name__ == "__main__":
    main()
