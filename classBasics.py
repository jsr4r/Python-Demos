import stdio
import math

# Author: Jonathan Reed
# Basic classes + inheritance in python

#base class shape:
class Shape:
    def __init__(self, objType):
        self.objType = objType
        return
    def printType(self):
        print(self.objType)

#class Rect inherits from Shape - I.e. Rect "is a" shape
class Rect(Shape): 
    def __init__(self, height, width, objType):
        Shape.__init__(self, objType)
        self.height = height
        self.width = width
        return
    def calcArea(self):
        area = self.width * self.height
        return area
    
#Class circle inherits from shape as well
class Circle(Shape):
     def __init__(self, radius, objType):
        Shape.__init__(self, objType)
        self.radius = radius
        return
     def calcArea(self):
         area = radius * radius * math.pi
         return area

#instantiate a Rect object
square = Rect(2, 2, "Rect")
#function from child class
area = square.calcArea()
#function from parent class, accessed through Rect object (which is a shape!)
square.printType()
