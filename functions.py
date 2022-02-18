# This will calculate the minutes and second in a specific day,
# this is how function workes in python.
calculate_seconds =  24 * 60 * 60;
time_unit = 'minutes'


def time_calculation(days):
    print(f'{days} days have {days * calculate_seconds} {time_unit}')
   


time_calculation(20);
time_calculation(21);

time_calculation(22);
time_calculation(200);
time_calculation(2.51);




