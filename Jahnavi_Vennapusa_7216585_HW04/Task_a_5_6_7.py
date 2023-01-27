'''
How to get the dates of yesterday, today
and tomorrow?

'''

import numpy as np
today_time = np.datetime64('today', 'D')
yesterday_time = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
tomorrow_time =np.datetime64('today', 'D') + np.timedelta64(1, 'D')

print("Today time is:")
print(today_time)
print("Yesterday time is:")
print(yesterday_time)
print("Tomorrow time is:")
print(tomorrow_time)


'''
Extract the integer part of a random array 
using 5 different methods
'''

arr = np.random.uniform(0,10,10)
print("The uniform array is")
print('arr:\n',arr)
print ("First way:",arr-arr%1)
print ("Second way:",np.floor(arr))
print ("Third way:",np.ceil(arr)-1)
print ("Fourth way:",arr.astype(int))
print ("Fifth way:",np.trunc(arr))


'''
Create a structured array representing a 
position (x,y) and a color (r,g,b)

'''
#Taking zeroes from the array with np.zeroes
str_arr = np.zeros(10, [ ('position', [ ('x', float, 1),
                                   ('y', float, 1)]),
                    ('color',    [ ('r', float, 1),
                                   ('g', float, 1),
                                   ('b', float, 1)])])
print("Structured array is:",str_arr)

