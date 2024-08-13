import random
print("Welcome to employee wage computation program")

def check_attendance(attendance):
    if attendance==0:
        print('employee is absent')
        dailywage=0
        print(dailywage)
    if attendance==1:
        print('employee is present')
        dailywage=20*8
        print(dailywage)
num=random.randint(0,1)
check_attendance(num)