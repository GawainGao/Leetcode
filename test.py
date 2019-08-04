from functools import reduce 
a = 3
print(a)
a = 4 if 0 else "#"
print(a)

a = 4 if 1 else "#"

li = reduce (lambda x, y, z : x+y+z , [1,2,3,4,5,6])
print(li)



print(a)
