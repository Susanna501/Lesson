
'''FOR'''
# names = ['Artur','Vahag','Ani']
# for i in names:
# 	print(i)


# '''FOR- BREAK'''
# for i in 'python':
# 	if i == 'o':
# 		break
# 	print('Current letter:',i)


# '''FOR- BREAK'''
# var = 10
# while var > 0:
# 	print("Current letter: ",var)
# 	var = var-1
# 	if var == 5:
# 		break
# print('Good job')

'''FOR- Continue'''
# var = 10
# while var > 0:
# 	var = var-1
# 	print("Current letter: ",var)
# 	if var == 5:
# 		continue

# print('Good job')


# for x in range(7):
# 	print(x)

# for i in range(2,30):
# 	print(i)

# for y in range(0,100,5):
# 	print(y)



# name = 'abkcdk'
# for i in range(100,1,-10):
# 	print(i)

# c = len(name)
# for i in range(c):
# 	print(i)	

# color = 'XQKS'
# fruits = '2345678910'
# for x in color:
# 	for y in fruits:
# 		print(x,y)


# n = 1

# while n < 6:
# 	print('Susik')
# 	n += 1

# count = 0
# while True:
# 	print('Susik')
# 	count += 1
# 	if  count == 2:
# 		break



import random
count_pc = 0
count_user = 0

while True:

	pc = random.randint(1,5)
	user = int(input('number '))

	if  user == pc:
		count_user += 1
		print('good pc',pc,'user', user, 'count', count_user)	

	else:
		count_pc += 1
		print('bad pc',pc,'user', user, 'count', count_pc)	
		
	if count_user == 3:
		print('win user count-', count_user)
		break

	elif count_pc == 3:
		print('win pc count-', count_pc)	
		break	
			


# i = 0
# while i < 6:
# 	i += 1
# 	if i == 3:
# 		continue

# 	print(i)


# n = 5
# while n > 0:
#     n = n - 1
#     if n == 2:
#         break
#     print(n)
# print("Loop is finished")


# var = 5
# while var > 0:
# 	# print("Current letter: ",var)
# 	var = var-1
# 	if var == 2:
# 		break
# 	print("Current letter: ",var)
# print('Good job')

# n = 5
# while n > 0:
#     n = n - 1
#     if n == 2:
#         continue
#     print(n)
# print("Loop is finished")

# number = 0

# for number in range(10):
#     if number == 5:
#         break    # break here

#     print('Number is ' + str(number))

# print('Out of loop')

# i = 1
# while i < 6:
# 	print(i)
# 	if i == 4:
# 		break
# 	i += 1