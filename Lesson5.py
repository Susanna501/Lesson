# 6x^2 + 10x - 1 = 0
# D = b^2 - 4ac 
# x1, x2 = -b +- sqrt(D)/2a

# from math import sqrt, pi
# import random

'''Task1'''
# a = 6
# b = 10
# c = -1
# D = b**2 - 4 * a * c
# x1 = (-b + sqrt(D))/(2 * a)
# x2 = (-b - sqrt(D))/(2 * a)
# print(x1,x2)	


'''Task2'''
#c = 2pr
# r = 5
# c = 2 * pi * r
# print(c)

'''Task3'''
# name1 = random.randint(1,100)
# name2 = random.randint(1,100)
# print('Susik',name1,'Arno',name2)
# print('Susik',name1 > name2)


# question1 = input("when has happened the Avarayr's battle\n a)320 b)180\n c)451 d)127\n") == 'c'
# print(question1)

'''Lesson 5-tasks'''

import math
print(math.pi)
print(math.sqrt(49))


# from math import *
# print(pi)


import random
print(random.random())
print(random.randint(0,20)) # random.randint-patahakan kvercni 0-20 tveric 
x = 'abcdefgh'
print(random.choice(x))     # random.choice -patahakanu kvercni x popoxakani tareric meky


import random as r   		 # as -ov karoxne enq random in kam importi cankacac parametrin anun /alias tanq
print(r.randrange(0,100,3))  # randrange mijakayqna 0-n skizbn e, 100 verjy , isk 3-y qani qayl y mek e poxum


import time
print('Hi Susik')
time.sleep(7)
print('Hi Ani')


import os
print(os.getcwd())


import calendar
y = int(input('Input the year: '))
m = int(input('Input the month: '))
print(calendar.month(y,m))


import datetime
x = datetime.datetime.now()
print(x)
print(datetime.date.today())

z = (datetime.datetime(2021,5,17))
print(z)

y = datetime.datetime.now()
print(y.year)				# y.year veradardznum e taretivy 
print(y.strftime('%A'))		# y.strftime('%A') veradardznum e shabatva ory 



