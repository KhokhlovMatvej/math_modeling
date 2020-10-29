#import lec4_create_func
x0=10 #Переменная в глобальной области видимости
def move(t): #Локальная переменная
  x=x0*t
  return x 
print(move(3))
#print(x)

x='хорошо'
def my_func():
  x='плохо'
  print(x)
my_func()

print(x)








