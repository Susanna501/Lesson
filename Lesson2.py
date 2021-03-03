watch = input("Do you have a Rollex? ")
# res = watch.upper()== 'Y'
res = watch.lower()== 'y'
print('Yes',res)

phone = input('Do you have an Iphone? ')=='y'
color = input('Which is color your phone? ')== 'red'
model = int(input('Your phone model? '))== 12
# print(0.1+0.2==0.3)
print(phone,color,model)

r = float(input('R: '))
c = 2*3.14*r
print(c)

number = float(input('Number? '))
percent = float(input('% '))
result = number * percent/100
print(result + number)

number = float(input('Number? '))
sale = float(input('sale '))
res = number - number * sale/100
print(res)

a = float(input('1st '))
b = float(input('2nd '))
c = (a ** 2 + b ** 2)** 0.5
print(c)


x = 5
print(type(x))
y = 4.5
print(type(4.5))
name = 'George'
print(type(name))

