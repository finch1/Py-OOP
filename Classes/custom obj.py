# the blue print jeans
"""
Py constructor method for creating new objects; custom__init__ can define
unique parameters for a new object.
self - when a method is called on an object, Python automatically passes that
object as the first argument"""

class Jeans:
# __init__ is like the constructor
# self is a pointer to the obj
    def __init__(self, waist, length, color):
        self.waist = waist
        self.length = length
        self.color = color
        self.wearing = False

    def put_on(self):
        print('Putting on {}x{} {} jeans'.format(self.waist, self.length, self.color))
        self.wearing = True

    def take_off(self):
        print('Taking off {}x{} {} jeans'.format(self.waist, self.length, self.color))
        self.wearing = False

thisJeans = Jeans(31, 32, "blue")

class Vehicle: # base vehicle class
    def __init__(self, color, manuf):
        self.color = color
        self.manuf = manuf
        self.gas = 4 # a full tank of gas

    def drive(self):
        if self.gas > 0:
            self.gas -= 1
            print('The {} {} goes WHSSSHHH'.format(self.color, self.manuf))
        else:
            print('The {} {} sputters out of gas.'.format(self.color, self.manuf))

class Car(Vehicle): # inherets from Vehicle class
    # turn the radio on
    def radio(self):
        print("Rockin Tunes")
    # open the window
    def window(self):
        print("Cool breeze")

class Moto(Vehicle): 
    # inherets from Vehicle class
    # turn the radio on
    def speed(self):
        print("So Fast")
    # open the window
    def power(self):
        print("My face")

class eCar(Vehicle):
    def drive(self):
        print('The {} {} goes silent'.format(self.color, self.manuf))


vehicle1 = Car("blue", "Nissan")
vehicle2 = Moto("white", "Toyota")
vehicle3 = eCar("green", "Honda")


vehicle1.radio()
vehicle2.power()
vehicle3.drive()

import numpy as np
b = np.array(   [[[ 1,  2,  3, 4],
                    [ 4,  5,  6, 4]],

                [[ 7,  8,  9, 4],
                    [10, 11, 12, 4]]])

print("B HAS SHAPE: ",b.shape)
print(b[0])
print(b[0].shape)

# Lists like a garage
# 2d list of lists
# index cars by row, spot
            #col 0 ,  col 1, col 2
lot_2d = [  ['Toyota', 'Audi', 'BMW'],  # 0th row
            ['Lexus', 'Jeep'],          # 1st row
            ['Honda', 'Kia', 'Mazda']]  # 2nd row

# 3d list of lists of lists
# - index cars by floor, row, spot
lot_3d = [
            [['T', 'F', 'B'], # 0th floor   
             ['H', 'J'], 
             ['S', 'K', 'F']],

            [['S', 'N'],        # 1st floor
             ['V']],

            [['M','C'],         # 2nd floor
             [],
             ['V']]
                                                        ]

print(lot_2d[2][2])                                                        
print(lot_3d[2][2][0])    
for floor in lot_3d:
    for row in floor:
        for car in row:
            print(car)

import tkinter

def mouse_click(event):
    # retrieve XY coords as a tuple
    coords = root.winfo_pointerxy()
    print('coords: {}'.format(coords))            

root = tkinter.Tk()
root.bind('<Button>', mouse_click)
root.mainloop()

import queue
# a queue is optimized to handle FIFO transactions
q = queue.Queue(2)
print("empty",q.empty())
q.put("bag1")
print("empty",q.empty())
q.put("bag2")
print("full",q.full())
# q.put("bag3")
print(q.get())
print(q.get())
# print(q.get(False))
# print(q.get(False))

# a list is ideal for LIFO transactions as it is easier to append to the end
stack = list()
stack.append('item1')
stack.append('item2')
item = stack.pop()
stack.append('item3')
print(stack)

"""
Sets :
. Store groups of like objects
. Each item unique
. No order"""