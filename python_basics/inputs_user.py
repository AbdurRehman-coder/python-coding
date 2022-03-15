

# value1 = input('Enter first number: ');
# value1 = int(value1)
# value2 = input('Enter second number: ');
# value2 = int(value2)
# result = print(f'your answer is:  {value1 + value2}' )

# This program will take inputs from the user and will response according to it


calculate_units = 24 * 60 * 60
time_unit = 'seconds'
# Take inputs from the user and store it in [days_input]
# Inputs from the user are take as string so you can change
# it according to your needs
days_input = input('Enter the no. of days: ')

# Function to calculate the total seconds in no. days
def calculate_time_func(no_days) :
    print(f' days have: {no_days * calculate_units} {time_unit}')

# Return value from the function
def calculate_time_return(no_days) :
    return f'{no_days} days have: {no_days * calculate_units} {time_unit}'

converted_user_input = int(days_input)

# Calling to functions with user inputs arguments
calculate_time_func(converted_user_input)

return_value = calculate_time_return(converted_user_input)
print(return_value )
45