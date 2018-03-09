class student:
    def __init__(self):
        self.name='vishnu'
        self.age=20
        self.marks=900
    def talk(self):
        print('hi, I am' ,    self.name)
        print('my age is',    self.age)
        print('my marks are', self.marks)
s1=student()
s1.talk()
