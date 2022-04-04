#take input from user
list_values = []
# while loop
while (quit != 'q'):
    user_input = int(input('enter a number'))
    quit = input('Press q to stop')
    list_values.append(user_input)
# print the list
print(list_values)

# loop to find the average and product of entered values
i = 0
sum = 0
product = 1
while (i < len(list_values)):
    sum = sum + list_values[i]
    product = product * list_values[i]
    i += 1
average = sum / len(list_values)
print('Average is:', average)
print('Product of all values is: ', product)
