# Beispiel einer Vektorklasse

import math

class Vektor:

    def __init__(self,x=0.0,y=0.0):
        self.x=float(x)
        self.y=float(y)

    def __str__(self):
        return '({0:.2f},{1:.2f})'.format(self.x,self.y)

    def __getitem__(self,i):
        if type(i) != type(0):
           raise TypeError("Index keine ganze Zahl.")
        if i<0 or i>1:
           raise IndexError("Index nicht im zul. Bereich.")
        elif i==0:
           return self.x
        elif i==1:
           return self.y

    def __add__(self,other):
        if isinstance(other,Vektor):
           return Vektor(self.x+other.x,self.y+other.y)
        else:
           raise TypeError("Formate passen nicht.")

    def __mul__(self,other):
        if isinstance(other,Vektor):
           return self.x * other.x + self.y * other.y
        else:
           try:
              return Vektor(self.x * other, self.y * other)
           except TypeError:
              raise TypeError("Formate passen nicht.")

    def __rmul__(self,other):
        try:
           return Vektor(self.x * other, self.y * other)
        except TypeError:
           raise TypeError("Formate passen nicht.")

    def __abs__(self):
        return math.sqrt(self*self)   

    def copy(self):
        return Vektor(self.xx,self.y)

