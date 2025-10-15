from re import sub


class Employee:
    def __init__(self):
        self.__name = ""
        self.__age = 0
        self.__gender = ''
    
    def set_name(self, name : str):
        self.__name = name
    
    def set_age(self, age : int):
        self.__age = age
    
    def set_gender(self,gender: str):
        self.__gender = gender
    
    def get_info(self):
        print(f"{self.__name}")
        print(f"{self.__age}")
        print(f"{self.__gender}")

class Proffessor(Employee):
    def __init__(self):
        self.research_field = ""
        self.subjects = []
    
    def set_field(self,field: str):
        self.research_field = field
    
    def add_subject(self,subject: str):
        self.subjects.append(subject)

    def get_info(self):
        base = super().get_info()
        print(base)
        print(self.research_field)
        print(self.subjects)

class Staff(Employee):
    def __init__(self):
        self.depart = ""
    
    def set_depart(self,depart:str):
        self.depart = depart
    
    def get_info(self):
        base = super().get_info()
        print(self.depart)


# --- Test data section ---

# Create a Professor
p1 = Proffessor()
p1.set_name("Dr. Ahmed Ali")
p1.set_age(45)
p1.set_gender("Male")
p1.set_field("Artificial Intelligence")
p1.add_subject("Machine Learning")
p1.add_subject("Data Mining")

# Create a Staff member
s1 = Staff()
s1.set_name("Mona Youssef")
s1.set_age(35)
s1.set_gender("Female")
s1.set_depart("IT Department")

# Print info
print("Professor Info:")
p1.get_info()
print("\nStaff Info:")
s1.get_info()



