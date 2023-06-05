
'''
@Author: shubham shirke
@Date: 2023-06-05 12:32:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-05 12:57:30
@Title : Employee Wage Problem to calculate daily employee wage.
'''

import random

def check_attendance():
    """
    Description : This function generates a random number 0 or 1 using randint function and print employee is present or not.
    Parameters : none
    result : Print Employee is present or Absent
    """
    random_attendace_number = random.randint(0,2)   # generates a random number 0 or 1
    if random_attendace_number == 1:
        print("Employee is Present")
    else:
        print("Employee is Absent")
    
    return random_attendace_number

def calculate_daily_employee_wage(random_attendace_number):
    """
    Description : This function calcultes the daily wage of employee if he is present having wage per hour rate and full day hour of working.
    Paramenters : random_attendance_number  -  This number is returned from check_attendace() to check is employee is present or not.
    result : daily_wage - displays calculted daily wage if employee is present or absent.
    """
    wage_per_hour = 20
    full_day_hour = 8
    daily_wage = 0
    if random_attendace_number == 1:
        daily_wage = wage_per_hour * full_day_hour     # calcultes daily_wage
        print(f"Daily wage of the employee is: {daily_wage} $")
    else:
        print(f"Daily wage of the employee is:{daily_wage}$")


# main function
def main():
    random_attendace_number=check_attendance()
    calculate_daily_employee_wage(random_attendace_number)

# start Execution
if __name__ == "__main__":
    main()