
import math

class Complex():
    def __init__(self,real,imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if type(self) == type(other):
            return Complex(self.real + other.real, self.imag + other.imag)
        else:
            return Complex(self.real + other, self.imag)

    def __sub__(self, other):
        if type(self) == type(other):
            return Complex(self.real - other.real, self.imag - other.imag)
        else:
            return Complex(self.real - other, self.imag)
    def __mul__(self, other):
        if type(self) == type(other):
            real = self.real*other.real-self.imag*other.imag
            imag = self.imag * other.real + self.real * other.imag
            return Complex(real,imag)
        else:
            return Complex(self.real*other,self.imag*other)

    def __div__(self, other):
        if type(self) == type(other):
            top = self * other.conjugate()
            bottom = other.real ** 2 + other.imag**2
            return Complex(top.real/bottom,top.imag/bottom)
        else:
            return Complex(self.real/other,self.imag/other)

    def __truediv__(self, other):
        if type(self) == type(other):
            top = self * other.conjugate()
            bottom = other.real ** 2 + other.imag ** 2
            return Complex(top.real / bottom, top.imag / bottom)
        else:
             return Complex(self.real / other, self.imag / other)

    def conjugate(self):
        return Complex(self.real,-self.imag)

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imag ** 2)

    def __neg__(self):  # defines -c (c is Complex)
        return Complex(-self.real, -self.imag)

    def __str__(self):
        if(self.imag>=0):
            return "{}+{}i".format(self.real, self.imag)
        else:
            return "{}{}i".format(self.real, self.imag)
