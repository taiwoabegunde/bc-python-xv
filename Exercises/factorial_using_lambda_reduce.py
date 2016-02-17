from functools import reduce

num = 2
ls = range(1, num+1)
factorial = reduce(lambda x,y: x * y, ls)

print (factorial)