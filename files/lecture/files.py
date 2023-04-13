# Работа с файлами
# Каретка - Указатель - Курсор

# open(<Путь до файла>)
# file - open('/home/stateonuris/Python/makers/lessons') # абсолютный путь
# file = open('files.py') # относительный путь (относительно той директории в которой вы работаете)

# Режимы работы с файлами
# 1. Чтение -> r/r+ (read)
# 2. Запись -> w/w+ (write)
# 3. Добавления -> a/a+ (append)

# b, t, x

# file = open('text.txt')
# data = file.read() 
# data = data.split('\n')

# print(data)

# file.close()

# Контекстный менеджер
# with open('text.txt') as file:
#     data = file.readline()
    
#     print(data)
#     print(file.readline())
#     print(file, 'inside')

# print(file.read(), 'outside')


# file.tell() -> Возвращает индекс где находиться каретка
# file.seek(index) -> Перемещает курсор на индекс который вы передали

# with open('text.txt', 'r') as file:
#     print(file.readline().replace('\n', ''))
#     print(file.tell())
#     file.seek()
#     print(file.readline().replace('\n', ''))
    # file.read()
    # print(file.readline())

# with open('text.txt', 'r') as file:
#     print(file.readlines())

# with open('text.txt', 'w+') as file:
#     file.write('Petrvasya Strocha\n') 
#     file.write('Сендо Такеши\n') 
#     file.write('Рокки с запада\n') 
#     file.write('Макуноучи Иппо\n') 
#     file.seek(0)
#     print(file.tell())
#     data = ['Bilal is genuis!\n', 'Tima is good boy!\n']
#     file.writelines(data)

with open('text.txt', 'r+') as file:
    file.write('John Snow!')