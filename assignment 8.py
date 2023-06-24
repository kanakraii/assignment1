#single inheritance
class A:
    #paramterized constructor
    def __init__(self, a, b, c):
        self.__a = a
        self._b = b
        self.c = c

    def display(self):
        print("Values in class A:")
        print("a:", self.__a)
        print("b:", self._b)
        print("c:", self.c)


class B(A):
    def display(self):
        try:
            print("Values in class B:")
            print("a:", self.__a) 
             #exception 
        except AttributeError:
            print("ELEMENTS OF CLASS A CANNOT BE ACCESSED")
        print("b:", self._b)
        print("c:", self.c)

obj_a = A(0,1,2)
obj_b = B(2,3,4)

obj_a.display()
print()  
obj_b.display()
