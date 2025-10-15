from csv import Error
from random import Random
import random

class Person:
    def __init__(self):
        self.__first_name = ""
        self.__last_name = ""
        self.__age = 0
        self.__gender = ""
    
    def set_first_name(self,name : str):
        if not name:
            raise ValueError("[First Name] Enter a valid Name")
        self.__first_name = name

    def set_last_name(self,name: str):
        if not name:
            raise ValueError("[Last Name] Enter a valid Name")
        self.__last_name = name
    
    def set_age(self,age : int):
        if age <= 17:
            raise ValueError("Ineligible age. Only who is higher than 17 year-old can register")
        self.__age = age
    
    def set_gender(self,gender: str):
        gender = gender.lower()
        if not gender:
            raise ValueError("[gender] Enter a valid Gender")
        if gender.startswith('male') or gender.startswith("m"):
            self.__gender = "Male"
        elif gender.startswith ('female') or gender.startswith("f"):
            self.__gender = "Female"
        else:
            raise ValueError("plz enter either \"male\" or \"female\"\nnote: you can enter 'f' or 'm' idicating for female and male")
    
    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name
    
    def get_age(self):
        return self.__age
    
    def get_gender(self):
        return self.__gender
    
    def get_info(self):
        return f"""Name: {self.__first_name} {self.__last_name}
        Age: {self.__age}
        Gender: {self.__gender}"""


class Student(Person):
    def __init__(self):
        super().__init__()
        self.__id = 0
        self.__courses = []

    def set_student_id(self,id:int):
        self.__id = id
    
    def get_id(self):
        return self.__id

    def course_register(self,course_name: str):
        if course_name in self.__courses:
            raise ValueError("You already registered to this course before")
        self.__courses.append(course_name)
    
    def view_courses(self):
        return self.__courses
    
    def get_info(self):
        base_info =  super().get_info()
        return f"""{base_info}
        ID: {self.__id}
        Registered Courses: {self.__courses}"""
    
class Course:
    def __init__(self):
        self.__name = ""
        self.__code = ""
        self.__capacity = 100
        self.__students = []

    def set_course_name(self, name: str):
        if not name:
            raise ValueError("[Course] Enter a valid Course name")
        self.__name = name
    
    def set_course_code(self,code: str):
        if not code:
            raise ValueError("[Course] Enter a valid code")
        self.__code = code

    def get_course_name(self):
        return self.__name
    
    def get_course_code(self):
        return self.__code
    
    def get_course_students(self):
        return self.__students
    
    def enroll(self,student: Student):     
        if not self.__capacity:
            print(f"Course if Full. You Can't Register for {self.__name}")
            return
        student.course_register(self.__name)
        self.__students.append(student)
        self.__capacity -= 1
    
    def view_details(self):
        print("="*5, "Course Details", "=" * 5)
        print(f"Name: {self.__name}") 
        print(f"Code: {self.__code}")
        print(f"Available Places: {self.__capacity}")
        print(f"Students Enrolled:{self.__students}")
    
class University:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__ids = list(range(50000,100000))
        random.shuffle(self.__ids)
    
    def add_student(self, student: Student):
        if not len(self.__ids):
            raise Error("University is Full.")
        student.set_student_id(self.__ids.pop())
        self.__students.append(student)
    
    def add_course(self, course: Course):
        field = random.choice(["CS", "IS","AI"])
        number = random.randint(1,15)
        course.set_course_code(f"{field}{number}")
        self.__courses.append(course)
    
    def get_courses(self):
        return self.__courses
    
    def display_data(self):
        print("=" * 10, "University Data", "=" * 10)
        print("=" * 5,"📚 Courses", "=" * 5)
        for course in self.__courses:
            print(f"Name: {course.get_course_name()}")
            print(f"Code: {course.get_course_code()}")
        print("=" * 35)
        print("=" * 5,"👨‍🎓 Students", "=" * 5)
        for student in self.__students:
            print(f"{student.get_first_name()} {student.get_last_name()} (ID: {student.get_id()})")
        print("=" * 35)
    
    def report(self):
        print("=" * 10, "Courses Report", "=" * 10)
        for course in self.__courses:
            print(f"Name: {course.get_course_name()}\nCode: {course.get_course_code()}")
            print("=" * 5, "👨‍🎓 Students Enrolled", "=" * 5)
            for student in course.get_course_students():
                print(f"{student.get_first_name()} {student.get_last_name()}")
            print("=" * 34)
        print("=" * 34)