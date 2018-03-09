class student:
    #this is constructor
    def __init__(self,n='',m=()):
        self.name=n
        self.marks=m
    #this is an instance method
    def display(self):
        print('hi' ,    self.name)
        print('your marks are', self.marks)
#constructor is called without arguments
s=student()
s.display()
print('------------------')

#constructor is called with 2 arguments
s1=student('indu roopa',880)
s1.display()
print('------------------')



