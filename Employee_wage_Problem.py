
'''
@Author: shubham shirke
@Date: 2023-06-05 12:32:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-05 17:01:30
@Title : Employee Wage Problem to calculate employee wage till 20 working days or 100 working hours.
'''

import random

wage_per_hour = 20
full_day_hour = 8
part_day_hour = 4
max_monthly_days = 20
max_working_hour = 100

def generate_random_number():
    """
    Description : This function generates a random number 0 or 1.
    result : random number with value 0 or 1.
    """
    random_number = random.randint(0,2)
    return random_number

def calculate_employee_wage():
    """
    Description: This function computes employee wage for a month or max working hour for full time or part time employee.
    parameters : none
    result : monthly wage for part time or full time employee.
    """
    month_days = 0
    total_working_hour = 0
    daily_wage = 0
    month_wage = 0
    random_number_employee_type = generate_random_number()   #random number to choose full time or part time employee
    if(random_number_employee_type == 1):
        while (month_days != max_monthly_days or total_working_hour != max_working_hour):
            random_number_employee_attendance = generate_random_number() #random number for employee present or absent
            if(random_number_employee_attendance == 1):
                print("Full time Employee is Present")
                daily_wage = full_day_hour * wage_per_hour
                month_days +=1
                total_working_hour += full_day_hour
                month_wage +=daily_wage
                print(f"Daily wage of full time employee is:{daily_wage}$")
            else:
                print("Full time Employee is Absent")
                print(f"Daily wage of full time employee is:0$")
            if(month_days == max_monthly_days or total_working_hour == max_working_hour):
                break
        print(f"Monthly wage of full time employee is :{month_wage}$")
    else:
        while (month_days != max_monthly_days or total_working_hour != max_working_hour):
            random_number_employee_attendance = generate_random_number() #random number for employee present or absent
            if(random_number_employee_attendance == 1 ):
                print("Part time Employee is Present")
                daily_wage = part_day_hour * wage_per_hour
                month_days +=1
                total_working_hour += full_day_hour
                month_wage +=daily_wage
                print(f"Daily wage of part time employee is:{daily_wage}$")
            else:
                print("Employee Absent")
                print(f"Daily wage of part time employee is:0$")
            if(month_days == max_monthly_days or total_working_hour == max_working_hour):
                break
        print(f"Monthly wage of part time employee is :{month_wage}$")


# main function
def main():
    calculate_employee_wage()

# start Execution
if __name__ == "__main__":
    main()