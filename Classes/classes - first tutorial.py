# https://www.youtube.com/watch?v=v_Jp11xqCzg&list=PLzMcBGfZo4-l1MqB1zoYfqzlj_HH-ZzXt&index=1

# import stars = importing a module. Can contain classes
# s = stars.Star() = create a new instance of a Star object defined in stars. Star() = calling the constructor

class Dog(object): # created a new class inherets from object
    def __init__(self, name): # constructor. executes automaticly on new class instance
        print("New Dog Instance") # prints with every new class
        self._name = name # self is pointing to the instanciated class itself to tie that name variable with that object
    
    def speak(self): # self here allows this method to access the object's own properties
        print("Hi I am", self._name)
        pass

    def change_name(self, _new_name):
        self._name = _new_name

    def add_weight(self, weight):
        self._weight = weight

    def talk():
        print("bark")
        
tim = Dog("tim")
tim.speak()
tim.change_name("fred")
tim.speak()
# print(tim._weight) produces an error because weight has never been set for this object
tim.add_weight(3)
print(tim._weight)

class Cat(Dog): # the new Cat class inherets from Dog class = all attributes are transfered 
    def __init__(self, name, color): # this constructor is unique to Cat
        super().__init__(name) # calls the constructor of the parent and does the self initialization automatically
        self._color = color

        # overloading methods
    def talk():
        print("meow")        

mike = Cat("mike", "white")
mike.speak()

# general car class
class Car():
    def __init__(self, price, gas, color):
        self._price = price
        self._gas = gas
        self.color = color

    def fullTank(self):
        self._gas = 100
    def emptyTank(self):
        self._gas = 0

class Model(Car):
    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color)
        self._speed = speed

    def beep(self):
        print('Beep Beep')

class SportsModel(Model):
    def __init__(self, price, gas, color, speed, tire):
        super().__init__(price, gas, color, speed)
        self._tire = tire

    def beep(self):
        print('Vroom Vroom')

goodspeed = SportsModel(10, 1, 'b', 5, 4)
goodspeed.beep()

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

    def __add__(self, p): # built in functions. this works by adding two classes
        return self.x + p.x, self.y + p.y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    # some maths to find the length and compare points
    def length(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)

    def __gt__(self, p):
        return self.length() > p.length()
        

p1 = Point(5,4)
p2 = Point(1,1)

print(p1+p2)
print(p1)

class Dog():
    dogs = [] # static variable inside class. this is specific to the entire class of every dog object. Can be called with class name itself, not from an instantiated class

    def __init__(self, name):
        self.name = name # variable within a class, referenced by self.
        self.dogs.append(self) # append every dog object created to this list

    @classmethod # this decorator allows calling method directly with the name of the class
    def num_dogs(cls): # pass the class itself
        return len(cls.dogs)

    @staticmethod
    def bark(n): # no need to pass self or cls. its a simple output
        for _ in range(n):
            print("bark!")

print(Dog.num_dogs())

taz = Dog("taz")
print(taz.num_dogs())

rev = Dog("rev")
print(taz.num_dogs())

print(Dog.bark(3))