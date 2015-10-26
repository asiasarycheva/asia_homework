
def add(x, y):  #определяем функции
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

a = int(input ("first integer = ")) #вводим первое и второе число, вводим операцию, которую надо сделать
b = int(input ('second integer = '))
c = input ('operation (+,-,/,*) : ')


if c == '+': #вводим 4 варианта уравнений
    print ('result is', add(a,b))
if c == '-':
    print ('result is', a - b)
if c == '/':
    print ('result is', a/b)
if c == '*':
    print ('result is', a*b)

else print('invalid')
