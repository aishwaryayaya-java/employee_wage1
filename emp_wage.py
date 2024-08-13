import random
print("Welcome to employee wage computation program")
def check_attendance(attendance):
    match (attendance):
        case 0: 
            print("Employee is absent")
            dailywage=0  
            
        case 1: 
            print("Employee is present")  
            job=input("Enter full/part time :")
            match (job):
                case "full":
                    dailywage=20*8
                    
                case "part":
                    dailywage=20*4
    return dailywage                      
num=random.randint(0,1)
print(check_attendance(num))                   


"""
def check_attendance(attendance):
    if attendance==0:
        print('employee is absent')
        dailywage=0
        print(dailywage)
    elif attendance==1:
        print('employee is present')
        job=input("Enter part or full time :").lower()
        if(job=="part"):
            dailywage=20*4
        if(job=="full"):
            dailywage=20*8
        print(dailywage)
num=random.randint(0,1)
check_attendance(num)
"""