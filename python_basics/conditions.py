
from sqlite3 import converters


def calculate_seconds(no_days) : 
        return f'{no_days} days are {no_days * 24 * 60 * 60} seconds'
   

# Let's take the no_of_days from user
number_days = input('Enter the No. of days: \n')

# Validate the user input before excuting them
def validate_user_input():
    if number_days.isdigit(): 
        converted_number = int(number_days)
        if converted_number > 0 : 
            calculated_value = calculate_seconds(converted_number)
            print(calculated_value)
        else : 
            print('You have entered the zero (0) number')
    else : 
        print('you have entered invalid value, Please enter only digits')

# Calling to the validation method
validate_user_input()


x = 1
y = 2
x = y 
print(x)
print(y)