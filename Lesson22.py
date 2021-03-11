'''1. km to mile Write a python function which conversion kilometer to miles.'''
# def km_to_miles(km):
# 	return km / 1.6

# km = int(input('enter your number: '))

# print(km_to_miles(km))



'''2. Time Write a python function which conversion days to seconds.'''
# def days_to_second(days):
# 	return days * 24 * 60 *60

# days = int(input('enter your number: '))

# print(days_to_second(days))



'''3. Password Write a python function which generate a valid password.'''
# def my_password(password):

# 	number_count = 0
# 	for i in password:
# 		if i.isdigit():
# 			number_count +=1

# 	if password[0].isupper() and len(password)>= 8 and number_count > 1:   # password.istitle()- check Upper or lower
# 		return 'Valid password'
# 	else:
# 		return "Not Valid"

# pas = input('enter your pass: ')

# print(my_password(pas))



'''4. Factorial Factorial'''
# def my_fact(factorial):
# 	count = 1

# 	for i in range(1,factorial + 1):
# 		count *= i
# 	return count

# print(my_fact(6))


'''5. Max Given an list of numbers. Find the maximum element in list.Without use max function'''
# def my_list_max(maximum):
# 	maximum.sort()
# 	return maximum[-1]

# maximum = [126,30,-50,-2,220]
# print(my_list_max(maximum))

