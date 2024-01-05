#no Function
#no Class

import math

num_1 = 5
num_2 = 16

#add

add = num_1 + num_2
sub = num_1 - num_2
mult = num_1 * num_2

if num_2 == 0:
    raise ValueError('you can not divid, because of division by zero!')
div = num_1 / num_2

power = num_1 ** num_2
logarithm = math.log(num_1, num_2)



print('add: ', add)
print('sub: ', sub)
print('mult: ', mult)
print('div: ', div)
print('pow: ', power)
print('log: ', logarithm)
