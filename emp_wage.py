import random

class EmployeeWage:
    
    wage_hr = 20
    full_hr = 8
    part_hr = 4
    max_hr = 100
    max_days = 20
    
    def calculate_monthly_wage(self):
        total_wage = 0
        total_hrs = 0
        total_days = 0
        
        while total_hrs < self.max_hr and total_days < self.max_days:
            attendance = random.randint(0, 1)
            if attendance == 0:
                continue
            
            job = input('Enter the type of job (full/part): ').lower()
            
            if job == 'part':
                hrs = self.part_hr
            elif job == 'full':
                hrs = self.full_hr
            else:
                print("Invalid job type. Please enter 'full' or 'part'.")
                continue
            
            if total_hrs + hrs > self.max_hr or total_days >= self.max_days:
                break
            
            total_hrs += hrs
            total_days += 1
            total_wage += self.wage_hr * hrs
        
        print("Total working days:", total_days)
        print("Total working hours:", total_hrs)
        print("Total monthly wage:", total_wage)


EmployeeWage().calculate_monthly_wage()

#we can skip using self we need to use cls and @classmethod decorator




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



