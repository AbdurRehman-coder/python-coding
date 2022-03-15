
# Libraries are the large functions or classes that are written
# by other programmers and we just call it into our program
# in order to use it is functionality or some part of it.

# import math library to do math operation

# import math
# print('the value of pi is: ', math.pi)
# print(math.sqrt(9))

# # import statistic library to use basic statistic operations
# import statistics
# a = [100, 200, 300,4, 5]
# print(statistics.median(a))


# Number = 1

# while(Number <= 100):
#     count = 0
#     i = 2
    
#     while(i <= Number//2):
#         if(Number % i == 0):
#             count = count + 1
#             break
#         i = i + 1

#     if (count == 0 and Number != 1):
#         print(" %d" %Number, end = '  ')
#     Number = Number  + 1


for num in range(100):
    if num > 1:
        for i in range(2, num):
            if (num % i == 0):
                break
        else:
            print(num)