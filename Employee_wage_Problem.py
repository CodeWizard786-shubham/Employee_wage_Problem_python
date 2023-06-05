
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
    random_attendance_number = random.randint(0,2)   # generates a random number 0 or 1
    if random_attendance_number == 1:
        print("Employee is Present")
    else:
        print("Employee is Absent")
    
    return random_attendance_number

def calculate_daily_employee_wage_full_time(random_attendance_number,wage_per_hour,full_day_hour):
    """
    Description : This function calcultes the daily wage of full time employee if he is present having wage per hour rate and full day hour of working.
    Paramenters : random_attendance_number  -  This number is returned from check_attendace() to check is employee is present or not.
    result : daily_wage - displays calculted daily wage if full time employee is present or absent.
    """
    daily_wage_full_time = 0
    if random_attendance_number == 1:
        daily_wage_full_time = wage_per_hour * full_day_hour     # calcultes daily_wage
        print(f"Daily wage of the Full time employee is: {daily_wage_full_time} $")
    else:
        print(f"Daily wage of the Full time employee is:{daily_wage_full_time}$")


def calculate_daily_employee_wage_part_time(random_attendance_number,wage_per_hour,part_day_hour):
    """
    Description: This function calculates the daily wahe for part time employee whose working hours are 4.
    Parameters: random_attendace_number - contains value 0 to 1 from check_attendace().
                wage_per_hour  - wage per hour for employee.
                part_day_hour - working hours for part time employee.
    result : Daily_wage_part_time for part time employee.
    """
    daily_wage_part_time = 0
    if random_attendance_number == 1:
        daily_wage_part_time = wage_per_hour * part_day_hour     # calcultes daily_wage for part time employee
        print(f"Daily wage of the Part time employee is: {daily_wage_part_time} $")
    else:
        print(f"Daily wage of the Part time employee is:{daily_wage_part_time}$")

# main function
def main():
    wage_per_hour=20
    full_day_hour=8
    part_day_hour=4
    choice = int(input("Enter 1: Full time Employee \n 2: Part time Employee: \n Enter Choice: "))
    if choice == 1:
        random_attendace_number=check_attendance()
        calculate_daily_employee_wage_full_time(random_attendace_number,wage_per_hour,full_day_hour)
    elif choice == 2 :
        random_attendace_number=check_attendance()
        calculate_daily_employee_wage_part_time(random_attendace_number,wage_per_hour,part_day_hour)
    else:
        print("entered option is incorrect. Please enter 1 for full time employee or 2 for part time employee")


# start Execution
if __name__ == "__main__":
    main()