"""def func(arg1,*vartuple):
    print(arg1)
    for var in vartuple:
        print(var)

    return
func(10)
func(10,20,30,40)
def percentage(*args):
    sum=0
    for i in args:
        sum+=i
    avg=sum/len(args)
    print(avg,"avg")
percentage(10,20,30,40,50)
"""
"""def perc(**kwargs):
    s=0
    for i in kwargs:
     sub=i
     marks=kwargs[i]
     print(sub,"=",marks)

perc(math=77,physics=65,chem=78)   




sentence='this,is,not,as,hard,as,you,think,it,is'
D=dict()
for word in sentence.split(','):
    for char in word:
        if char not in D:
            D[char]=0
        D[char]+=1
mchar,mval='',0
alpha='abcdefghijklmnopqrstuvwxyz'
for char in alpha:
    if char not in D:
        continue
    if D[char]>=mval:
        mval=D[char]
        mchar=char
print(mchar)"""


class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        return self.model,self.brand    

class Car(vehicle):
    def __init__(self, brand, model,seating_capacity):
        super().__init__(brand, model)
        self.seating_capacity=seating_capacity
    def display_car(self):
        print( super().display())
        print(self.seating_capacity)
class electric_car(Car):
    def __init__(self, brand, model, seating_capacity,battery_capacity):
        super().__init__(brand, model, seating_capacity)
        self.battery_capacity=battery_capacity
    def display_elec(self):
        print(super().display_car())
        print(self.battery_capacity)
car=electric_car("honda","city",4,48)
print(car.display())
print(car.display_car())
print(car.display_elec())