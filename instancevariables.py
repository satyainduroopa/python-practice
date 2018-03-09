class sample:
    #this is constructor
    def __init__(self):
        self.x=10

    #this is an instance method
    def modify(self):
        self.x+=1

#create 2 instances
s1=sample()
s2=sample()
print('x in s1=',s1.x)
print('x in s2=',s2.x)

#modify x in s1
s1.modify()
print('x in s1=', s1.x)
print('x in s2=', s2.x)



#output
E:\py>instancevariables.py
x in s1= 10
x in s2= 10
x in s1= 11
x in s2= 10