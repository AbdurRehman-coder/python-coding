
def calculate_seconds(no_days) : 
    if no_days > 0 :
        return print(f'{no_days} days are {no_days * 24 * 60 * 60} seconds')
    elif no_days == 0 :
        print('You have entered the zero (0) number')

# Let's take the no_of_days from user
number_days = input('Enter the No. of days: \n')

# Validate the user input before excuting them
def validate_user_input():
    if number_days.isdigit(): 
        calculated_value = calculate_seconds(int(number_days))
        print(calculated_value)
    else : 
        print('you have entered invalid value, Please enter only digits')

# Calling to the validation method
validate_user_input()


