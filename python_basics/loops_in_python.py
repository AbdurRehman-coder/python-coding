# while and for_loops 

# while loop 
x = 2 
while x < 10 :
    print('x: {}'.format(x))
    x = x + 1

# for loop
name_list = ['rehman', 'yasir', 'abid']
for n in name_list:
    if n == 'yasir': continue
    print(n)

# Loop through String
name = 'Abdur Rehman Shinwari'
for n in name:
    if n == 'R': break
    print(n)

# loops in some range
# for n in range(5): # it start from zero (0) by default and the no. 5 is not inculded
#     print(n)

# it will start from 3 upto 9, 10 not included
for number in range(3, 10):  
    print(number)  # /n for new line

print('\n\n\n')

#loop start from 2 and upto 20, take 3 step after each iteration
for n in range(2, 20, 3):
    print(n)