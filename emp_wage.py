import random
print("Welcome to employee wage computation program")

def check_attendance(attendance):
    if attendance==0:
        print('employee is absent')
    if attendance==1:
        print('employee is present')
num=random.randint(0,1)
check_attendance(num)