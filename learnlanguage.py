'''
a, b, c, d, e = 100, 12.23, 1+5j, 'hello world', True

print('type(a) = {0},type(b) = {1},type(c) = {2},type(d) = {3},type(e) = {4},'.format(type(a),type(b),type(c),type(d),type(e)))


flag1 = 3>2
print(flag1 is True)
print(flag1 == True)



from math import *
radius = 1
while radius != 0:
    radius = float(input('radius='))
    perimeter = 2*pi*radius
    area = pi*radius*radius
    print('perimeter={},area={}'.format(perimeter, area))



year = 1
while year != 0:
    year = int(input('year='))
    is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
    print(is_leap)

'''
