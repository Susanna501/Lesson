'''Write a Python program to find the smallest number which are divisible by 12 and 15.'''
num1 = int(input("number1:" ))
num2 = int(input("number2:" ))
end = num1 * num2 + 1

if num1 > num2:
	start = num1
else:
	start = num2

count = 0

for i in range(start, end):
	count += 1
	if i % num1 == 0 and i % num2 == 0:
		print(i, count)
		break


'''Write a Python program to count the number of even
and odd numbers from a series of numbers(1-100).'''
num = int(input("number1:" ))
count_even = 0
count_odd = 0
end = num + 1

for i in range(1,end):
	if i % 2 == 0:
		count_even += 1
	
	else:
		count_odd +=1

print('even',count_even, 'odd',count_odd)		


num = int(input("number1:" ))
if num % 2 ==0:
	count_even = count_odd = num / 2
else:
	count_even = num // 2
	count_odd = num // 2 + 1

print('even',count_even, 'odd',count_odd)	



'''Write a Python program that accepts a string and calculate the number
of digits and letters. string = ‘python 3.9’'''

# string = 'python 3.9'
# count_letter = 0
# count_digit = 0

# for i in string:
# 	if i.isalpha():
# 		count_letter  += 1
# 	elif i.isdigit():
# 		count_digit +=1
	
# print('letter',count_letter, 'digit', count_digit)


'''Write a Python program which have number (73421):
You should calculate (7 + 3 + 4 ….):'''

# my_number = int(input("number:" ))
# count = 0

# for i in str(my_number):
# 	count += int(i)

# print(count)


'''Write a loop to find the factorial of any number. You have one input.'''

# my_number = int(input("number:" ))
# count = 1
# end = my_number + 1

# for i in range(2, end):
# 	count *= i
# 	print(count, i)
	

