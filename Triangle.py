class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def is_valid(self):
        if self.a+self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return ('Valid')
        else:
            return ('Invalid')
        
    def Side_Classification(self):

            if self.a == self.b == self.c:
                return('Equilateral')
            elif self.a == self.b or self.a == self.c or self.b == self.c:
                return ('Isosceles')
            elif self.a != self.b != self.c:
                return('Scalene')
     
        
    def Angle_Classification(self):
  
            if self.a*self.a + self.b*self.b > self.c*self.c:
                return ('Acute')
            if self.a*self.a + self.b*self.b == self.c*self.c:
                return ('Right')
            if self.a*self.a + self.b*self.b < self.c*self.c:
                return ('Obtuse')
   
        
    def Area(self):
 
            s = (self.a + self.b + self.c)/2
            Area = (s*((s-self.a)*(s-self.b)*(s - self.c)))
        return Area
  
a=int(input())
b=int(input())
c=int(input())
T=Triangle(a,b,c)
print(T.is_valid())
print(T.Side_Classification())
print(T.Angle_Classification())
print(T.Area())
