import random  
print("Welcome to employee wage computation program")
wage_hr=20
full_hr=8
part_hr=4
max_hr=100
max_days=20
def monthly_wage():
    total_wage=0
    total_hrs=0
    total_days=0
    while total_hrs<max_hr or total_days<max_days:
        attendance=random.randint(0,1)
        if attendance==0:
          continue
        
        job=input('enter a type of job :').lower()     
        if job=='part':
          hrs=part_hr
              
        elif job=='full':
          hrs=full_hr
        else:
          print("give job type")
          continue       
         
        if total_hrs+hrs >= max_hr or total_days >= max_days:
          break
        total_hrs+=hrs
        total_days+=1
        total_wage+=wage_hr*hrs
            
    print( "Total working days are" ,total_days) 
    print("Total working hrs are'" ,total_hrs)           
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



