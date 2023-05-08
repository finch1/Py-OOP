# https://www.youtube.com/watch?v=0VdzZQdaZ28&list=PLzMcBGfZo4-nhWva-6OVh1yKWHBs4o_tv

def func(x=1):
    return x**2

print(func())
print(func(5))

class Car(object):
    def __init__(self, make, model, year, condition = 'New', kms=0) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms

    def display(self, showAll=True):
        if showAll:
            print("This car is a %s %s from %s, it is %s and has %s kms."
            %(self.make, self.model, self.year, self.condition, self.kms))
        else: print("This car is a %s %s from %s."
                    %(self.make, self.model, self.year))

car1 = Car("Honda", "Prelude", 2003)
car1.display(False)
car1.display()

# map function
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

newList = []
for x in li:
    newList.append(func(x))

print(newList)
# same as for loop
print(list(map(func,li))) # map function applies a predefined function on a list
print([func(x) for x in li]) # list comprehension
print([func(x) for x in li if x%2 == 0]) # list comprehension - even numbers

# filtering out elements in a list based on predefined function
def isOdd(x):
    return x%2 != 0

print(list(filter(isOdd, li)))
print(list(filter(lambda z: z%2 == 0, li))) # find even numbers in list

# lambda functions - anonimous function
def add_func(x):
    return x+5

add_func2 = lambda x: x+5 # anonimous function parameter: return value
print(add_func2(5))

add_func3 = lambda x,y: x+y
print(add_func3(5,5))

print(list(map(lambda a: a+1, li)))