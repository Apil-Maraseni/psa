# WAP to add two complex numbers using class and objects
class Complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag    

    def print_result(self):

        print(str(self.real)+ "+i"+str(self.imag))
    
    def calculate(self, c):
        self.real += c.real
        self.imag += c.imag

c1 = Complex(10,20)


c2 = Complex(20,30)
c2.print_result()

c1.calculate(c2)
c1.print_result()
