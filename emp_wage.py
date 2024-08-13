import random
print("Welcome to employee wage computation program")
import random
def monthly_wage():
    total_wage=0
    for i in range(20):
        attendance=random.randint(0,1)
        if attendance==0:
            continue
        if attendance==1:
            job=input('enter a type of job :').lower()
            if job=='part':
                total_wage=total_wage+(20*6)
            elif job=='full':
                total_wage=total_wage+(20*8)
            else:
                print("give job type")
    return total_wage

print("Total monthly wage:" ,monthly_wage())







# def check_attendance(attendance):
#     match (attendance):
#         case 0: 
#             print("Employee is absent")
#             dailywage=0  
            
#         case 1: 
#             print("Employee is present")  
#             job=input("Enter full/part time :")
#             match (job):
#                 case "full":
#                     dailywage=20*8
                    
#                 case "part":
#                     dailywage=20*4
#     return dailywage                      
# num=random.randint(0,1)
# print(check_attendance(num))                   



