# Работа с файлами

f = open('test.txt', 'w') # создается файл test.txt в текущей директории
# если test.txt существует, то он будет перезаписан

f.write("13456\n") # \n для перехода на новую строку
f.write("54444")
f.close()


f2 = open('test.txt', 'r') # на чтение, файл должен существовать
a = f2.read() # a = '13456\n54444'
b = f2.read() # b = '' пустая строка, т.к. уже все считали из файла
# решение - спец функция / повторное открытие файла
f2.close


f2 = open('test.txt', 'r')

for line in f2: # line принимает поочередно значения каждой строки из f2
    print('this is line: ' + line)

f2.close
