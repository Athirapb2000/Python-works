"""
Abstraction - is to represent the essential features without representing explanation or background details.
              Main advantage is data hiding
"""

from abc import ABC, abstractmethod
# abstract class
class Polygon(ABC):
    # abstract method
    @abstractmethod
    def sides(self):
        pass
    def display(self):
        print('non abstract method')
class Triangle(Polygon):
    def sides(self):
        print('Triangle has 3 sides')

t = Triangle()
t.sides()
t.display()
