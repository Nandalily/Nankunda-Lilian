# university system with parent class person and sub classes
# system displays their details

class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")


class Student(Person):
    def __init__(self, name, age, email, student_id, major, gpa):
        super().__init__(name, age, email)
        self.student_id = student_id
        self.major = major
        self.gpa = gpa
    
    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")
        print(f"Major: {self.major}")
        print(f"GPA: {self.gpa}")
        print("Role: Student")


class Lecturer(Person):
    def __init__(self, name, age, email, employee_id, department, courses_taught):
        super().__init__(name, age, email)
        self.employee_id = employee_id
        self.department = department
        self.courses_taught = courses_taught
    
    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")
        print(f"Courses Taught: {', '.join(self.courses_taught)}")
        print("Role: Lecturer")


class Staff(Person):
    def __init__(self, name, age, email, employee_id, position, responsibilities):
        super().__init__(name, age, email)
        self.employee_id = employee_id
        self.position = position
        self.responsibilities = responsibilities
    
    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")
        print(f"Position: {self.position}")
        print(f"Responsibilities: {self.responsibilities}")
        print("Role: Staff Member")


# Create instances of each class
student1 = Student("Alice Johnson", 20, "alice@uni.edu", "S1001", "Computer Science", 3.8)
lecturer1 = Lecturer("Dr. Smith", 45, "smith@uni.edu", "E2001", "Computer Science", ["Python Programming", "Algorithms"])
staff1 = Staff("Bob Wilson", 35, "bob@uni.edu", "E3001", "Administrator", "Student registration, Facility management")

# Display information for each person
print("\n=== Student Information ===")
student1.display_info()

print("\n=== Lecturer Information ===")
lecturer1.display_info()

print("\n=== Staff Information ===")
staff1.display_info()