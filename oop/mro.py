"""This script demonstrates MRO (Method Resolution Order) in OOP."""


class A():
    def __init__(self):
        super().__init__()
        self.foo = 'foo'
        self.name = 'Class A'


class B():
    def __init__(self):
        super().__init__()
        self.bar = 'bar'
        self.name = 'Class B'


class C(A, B):
    def __init__(self):
        super().__init__()
    
    def show_prop(self):
        print(self.foo)
        print(self.bar)
        print(self.name)


c_instance = C()
c_instance.show_prop()
print('Now printing the Method Resolution Order for Class C is {}.'.format(C.mro()))