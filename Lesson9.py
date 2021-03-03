'''You have number. Write a python program which to print a new number with digits 
reversed as of original one. 
For example:
INPUT : 1234        OUTPUT : 4321
INPUT : 5982        OUTPUT : 2895'''

# number = int(input('my number: '))
# first = number % 10
# second = number % 100 // 10
# third = number % 1000 // 100
# forth = number // 1000
# print(int(str(first)+str(second)+str(third)+str(forth)))

# print('1234'[::-1])

'''You and the Pc take part in the rally, 
You must pass 12 km. PC passed in 3 minutes and You are 10% later than Pc. 
how much is the speed of your car.'''

# km = 12
# time = 3 * 0.1 + 3
# user_speed = km/ time
# print(user_speed)


'''You (input) and pc have followers (pc have random followers) if your followers
is great 20 % than pc you are blogger otherwise pc is blogger.'''

import random
pc = random.randint(1,300)
user = 200
if user > pc + pc * 0.2:
	print(user, 'Blogger')
else:
	print('Pc is blogger',pc)


