# This will calculate the minutes and second in a specific day,
# this is how function workes in python.
calculate_seconds =  24 * 60 * 60;
time_unit = 'minutes'

#function definition and its body
def time_calculation(days):
    print(f'{days} days have {days * calculate_seconds} {time_unit}')

def scope_check(days, message) :
    print(days)  
    print(message) 

#Call to function
time_calculation(20);
time_calculation(21);
time_calculation(200);
time_calculation(2.51);

#call to scope function, where we just checking the scop of variable
scope_check(180, 'variable scope')




