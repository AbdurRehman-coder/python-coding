# find prime number between range of numbers
# take inputs from user
start_value = int(input('Enter the start value: '))
end_value = int(input('Enter the end value: '))

# for loop to start from start to end value
for number in range(start_value, end_value + 1):
    if number > 1: 
        # it will start from 2 to minus that specfic number which check is it prime or not
        for i in range(2, number):
            # if number divide equally any of that number, mean it is not prime number, So break it
            if (number % i == 0):
                break
        else:
            print('prime number: %s'%number)
