'''
@Author: shubham shirke
@Date: 2023-06-05 12:32:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-05 13:35:30
@Title : Employee Wage Problem to get monthly wage and total working hour with seperate working hour function .
'''

import random

wage_per_hour = 20
full_day_hour = 8
part_day_hour = 4
max_monthly_days = 20
max_working_hour = 100
is_full_time = 1
is_part_time = 2
is_absent = 0

def generate_random_number():
    """
    Description: This function generates a random number 0 or 1 or 2.
    Returns: Random number with value 0 or 1 or 2.
    """
    random_number = random.randrange(3)
    return random_number

def get_work_hours(employee_working_type):
    """
    Description: This function calculates the work hours based on the employee type.
    Parameters:
        - employee_working_type: 0 for absent,1 for full time, 2 for part time
    Returns: Total work hours
    """
    total_work_hour = 0
    if employee_working_type == is_full_time:
        print("Full time employee is present")
        total_work_hour += full_day_hour
    elif employee_working_type == is_part_time:
        print("Part time employee is present")
        total_work_hour += part_day_hour
    elif employee_working_type == is_absent:
        print("Employee is absent")
        total_work_hour += 0
        

    return total_work_hour

def calculate_employee_wage():
    """
    Description: This function computes the employee wage for a month or max working hour for a full-time or part-time employee.
    Parameters: none
    result : montly wage of the employee along with total working hour.
    
    """
    month_days = 0
    month_wage = 0
    total_work_hour = 0
    daily_wage = 0
    absent_wage = 0

    while month_days != max_monthly_days or total_work_hour != max_working_hour:
        employee_working_type = generate_random_number()
        if employee_working_type == is_full_time:
            daily_wage = full_day_hour * wage_per_hour
            month_wage += daily_wage
            month_days += 1
            total_work_hour += get_work_hours(employee_working_type)
            print(f"Daily wage of full-time employee is: {daily_wage}$")
        elif employee_working_type == is_part_time:
            daily_wage = part_day_hour * wage_per_hour
            month_wage += daily_wage
            month_days += 1
            total_work_hour += get_work_hours(employee_working_type)
            print(f"Daily wage of part-time employee is: {daily_wage}$")
        else:
            daily_wage = absent_wage * wage_per_hour
            month_days +=1
            month_wage += daily_wage
            total_work_hour += get_work_hours(employee_working_type)
            print(f"Daily wage of employee is:{daily_wage}$")
        if(month_days == max_monthly_days or total_work_hour == max_working_hour):
            break
    
    # print monthly wage and total working hour
    print()
    print(f"Monthly wage of Employee is: {month_wage}$")
    print(f"Total working time of Employee is: {total_work_hour}")

# main
def main():
    calculate_employee_wage()


if __name__ == "__main__":
    main()
