
'''
@Author: shubham shirke
@Date: 2023-06-05 12:32:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-05 12:32:30
@Title : Employee Wage Problem to check Employee is present or absent.
'''

import random

def check_attendance():
    """
    Description : This function generates a random number 0 or 1 using randint function and print employee is present or not.
    Parameters : none
    result : Print Employee is present or Absent
    """
    random_attendace_number = random.randint(0,2)   # generates a random number 0 or 1
    if random_attendace_number == 0:
        print("Employee is Present")
    else:
        print("Employee is Absent")

# main function
def main():
    check_attendance()

# start Execution
if __name__ == "__main__":
    main()