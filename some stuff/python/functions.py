# Функции

def my_function(name):
    #print("hello", name)
    return "hello " + name

tmp = my_function("Ann")
print(tmp)
print(my_function('Me'))


gl = 6 # gl - глобальная переменная, можно использовать внутри функций
def other_function():
    local = 5 # local - локальная переменная, вне функции не будет видна
