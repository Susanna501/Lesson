'''1. New List Create new list which have 5 different data types.'''
# num = [5, 'Susik', True, 63.3, (3,11), [1,33]]
# print(num)


'''Create new list which have data notebooks and you want check if
the data have macbook?'''

# data = ['asus', 'macbook','hp','Dell']
# if 'macbook' in data:
# 	print('yes')
# else:
# 	print('no')


'''Create python program which will check if your password is strong
or no. if Len your password is great than 8 and if your password have
2 numbers and 2 of the following special characters ('!', '@', '#', '$', '%',
'&', '*') Sample Input: Python@$World11
Sample Output: Strong'''

# password = input('please write your pass: ')
# sym = '!', '@', '#', '$', '%','&', '*'
# numbcount = 0
# sumcount = 0

# for i in password:
# 	if i.isdigit():
# 		numbcount +=1
# 	elif i in sym:
# 		sumcount += 1
# if numbcount > 1 and sumcount > 1 and len(password) > 8:
# 	print('strong')

'''or'''
# limit = 0
# char = '!@$%&#'
# password  = input('Password: ')

# while True:
	
# 	limit += 1
# 	if limit > 3:
# 		print('Pleaes try later you use 3 times')
# 		break

# 	number_count = 0
# 	char_count = 0
# 	password  = input('Try again Password: ')

# 	if password[0].islower():
# 		print('your firs letter must be upper')
# 		continue

# 	elif len(password) < 9:
# 		print('Your password length is less than 8' )
# 		continue

# 	for i in password:
# 		if i.isdigit():
# 			number_count += 1
# 		elif i in char:
# 			char_count += 1

# 	if number_count < 2:
# 		print('Your password must be have 2 or more numbers')
# 		continue

# 	elif char_count < 2:
# 		print('Your password must be have 2 or more chars',char)
# 		continue
# 	else:
# 		print('Your password is strong')
# 		break


'''Create python program where you want to find id in link if link have id print id.
Sample Input: https://www.youtube.com/watch?v=RRW2aUSw5vU
Sample Output: RWW2aUSwvU'''


# idner = input('please write your pass: ').split(",")
# print(idner)
# count =0

# for i in idner:
# 	count +=1
# 	if i == '=':
# 		break
# print(idner[count:])

# '''or '''
# link = input('Link: ').split("=")
# print(link[1])
# # print(link[link.index('=')+1:])
# print(link)



