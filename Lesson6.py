
x = 4
x < 5 and x < 10  # and operator (2 is true)
print(x < 5 and x < 10 )

x < 5 and x > 10  # or operator (1 of this true)
print(x < 5 or x < 10 )

not(x < 5 and x < 10)  # not operator (reverse result)
print(not(x < 5 and x < 10 ))

a = 'h'
b = 'h'
a is b
print(a is b)

a = 'hello'
b = 'banana'
a is not b
print(a is not b)

a = 'banana'
res_true = 'n' in a
res_false = 'k' in a
print(res_true)
print(res_false)

a = 'hello'
res_false = 'l' not in a
res_true = 'k' not in a
print(res_true)
print(res_false)


x = 5
print(id(x))



'''Task1'''
# post_code = input('email: ')
# res = '@' in post_code and '.' in post_code
# print('Valid email: ',res)


'''Task2'''
banana = input('banana: ')
res_banana = banana == 'y' or banana == 'yes'
print('banana:',res_banana)
# light = input('light: ')
# res_light = light == 'y' or light == 'yes'
# print('light:',res_light)
# res3 = res_banana and not res_light 
# print('hanel banana: ',res3)
# res4 = not res_banana 
# print('gnel banana: ', res4)


'''Task3'''
# user = input('only numbers: ')
# c = '1234567890'
# res = user in c 
# print(res)

