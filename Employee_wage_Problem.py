
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

def calculate_daily_employee_wage_full_time(wage_per_hour,full_day_hour):
    """
    Description : This function calcultes the daily wage of full time employee if he is present having wage per hour rate and full day hour of working.
                  for a month (20 days)
    Paramenters : wage_per_hour  - wage per hour for employee.
                  full_day_hour - working hours for full time employee.
    result : daily_wage - displays calculted daily wage if full time employee is present or absent.
    """
    daily_wage_full_time = 0
    monthly_wage_full_time = 0
    for _ in range(20):
        random_number=check_attendance()   # running check_attendance() 20 times and storing each number in varaible
        if random_number == 1:
            daily_wage_full_time = wage_per_hour * full_day_hour     # calcultes daily_wage
            monthly_wage_full_time += daily_wage_full_time
            print(f"Daily wage of the Full time employee is: {daily_wage_full_time}$")
        else:
            print(f"Daily wage of the Full time employee is:0$")
    print(f"Monthly wage of full time employee is : {monthly_wage_full_time}$")


def calculate_daily_employee_wage_part_time(wage_per_hour,part_day_hour):
    """
    Description: This function calculates the daily wahe for part time employee whose working hours are 4 for a month(20 days)
                 
    Parameters: wage_per_hour  - wage per hour for employee.
                part_day_hour - working hours for part time employee.
    result : Daily_wage_part_time for part time employee.
    """
    daily_wage_part_time = 0
    monthly_wage_part_time=0
    for _ in range(20):
        random_number=check_attendance()    # running check_attendance() 20 times and storing each number in varaible
        if random_number == 1:
            daily_wage_part_time = wage_per_hour * part_day_hour     # calcultes daily_wage for part time employee
            monthly_wage_part_time += daily_wage_part_time
            print(f"Daily wage of the Part time employee is: {daily_wage_part_time}$")
        else:
            print(f"Daily wage of the Part time employee is:0$")
    print(f"Monthly wage of part time employee is:{monthly_wage_part_time}$")



# main function
def main():
    wage_per_hour=20
    full_day_hour=8
    part_day_hour=4
    bool = True
    while(bool):
        choice = int(input("Enter \n 1: Full time Employee \n 2: Part time Employee: \n 3: Exit \n Enter Choice: "))
        if choice == 1:
            calculate_daily_employee_wage_full_time(wage_per_hour,full_day_hour)
        elif choice == 2 :
            calculate_daily_employee_wage_part_time(wage_per_hour,part_day_hour)
        elif choice == 3:
            bool = False
        else:
            print("entered option is incorrect. Please enter 1 for full time employee or 2 for part time employee")


# start Execution
if __name__ == "__main__":
    main()