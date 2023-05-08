# https://www.youtube.com/watch?v=JeznW_7DlB0


class Dog:
    
    def __init__(self, name): # self = object instantiated itself, an reference to the object instantiated so the code can access it. 
        self.name = name # we created an attribute name
        print(name)
        pass
            
    def add_one(self, x):
        return x + 1

    def bark(self):
        print("bark!!")

    def get_name(self):
        return self.name

    def set_name(self, _name):
        self.name = _name


p = Dog('Pipa') # this uses the __init__ constructor. this means the Dog object always requrires a name

print(type(p))
p.bark()
print(p.add_one(5))

p.set_name('Pippa')

print(p.get_name())


## CLASSES INTERACTING TOGETHER

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, course_name, max_students):
        self.name = course_name
        self.max_students = max_students
        self.students = [] # students object list related to the course. initialized with every course created

    def add_student(self, students): # add student object
        if len(self.students) <= self.max_students: # if the course still has room for students
            self.students.append(students)
            return True # added succesfully
        return False # not added

    def get_average_grade(self):
        grade = 0
        for s in self.students:
            grade = grade + s.get_grade()

        return grade / len(self.students)

s1 = Student("Tim",25,80)
s2 = Student("Bil",25,70)
s3 = Student("Jil",25,60)
s4 = Student("Fil",25,50)

science_course = Course("Science", 2)
b = bool

b = science_course.add_student(s1)
print(b)
b = science_course.add_student(s2)
print(b)
b = science_course.add_student(s3)
print(b)
b = science_course.add_student(s4)
print(b)

print(science_course.students[1].name)
print(science_course.get_average_grade())


## SOME MORE INHERETANCE
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what to say")

class Cat(Pet): # using brackets with inheretence. super class has not
    def speak(self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Horse(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age) # reference the constructor in the super class (Pet)
        self.color = color

    def speak(self):
        print("Brrr")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and my color is {self.color}")

p = Pet("Bill", 66)
p.speak()

c = Cat("Fill", 67)
c.speak()

d = Dog("Dug", 77)
d.speak()

h = Horse("Horace", 13, "brown")
h.show()

## CLASS Attributes
# attributes specific to the class and not the object

class Person:
    number_of_people = 0
    avg_age = 34 # class constant defined in person

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1 # increments everytime we add a new person

p1 = Person("corry")
p2 = Person("xevior")

print(Person.number_of_people)

Person.number_of_people = 9 # override the count
print(p2.number_of_people) # using the class attribute common to all classes

