# Области видимости и простраснства имен (scopes)
# технология которая определяет контекст имени (переменные )
# в рамках которого мы можем ее использовать
# build-ins (Встроенная область видимости) - > print, len, max

# global(Глобальная область видимости) -> Область одного файла
# enclosed(не локальная(замкнутая), nonlocal)
# local(локальная область) -> область внутри одной функции

# x = 200

# def my_func():
#     print(x)
#     a = 300
#     print('a=', a)
    
    
    
# my_func()
# print(x)
# # print(a)

# a = 10 # global

# print() # build-in

# def hello(): # global
#     a = 'Hello  world!' # local
#     print(a, 'local insade in func!')
    
# hello(a, 'global')

# LEGB - local enclosed global built-in

#----------------------------------------------
# Enclosed - замкнутое пространство имен
# Замкнутое просранство - это локальное пространство, у которого есть внутренее (вложенное) локальное пространство

# x = 'global'

# print(x)

# def print_x():
#     x = 'enclosed'
    
#     def local_func():
#         x = 'local'
        
#         print(x)
#     print(x)
#     local_func()
#     print(x)        

        
# print_x()
# print(x)
#----------------------------------------------
# a = 5

# def func():
#     print(a)

# func()
#----------------------------------------------

# global -> Позволяет изменять значения глобальной переменной находясь внутри локальной области видимости
# nonlocal -> Позволяет изменять значения не локальной (замкнутой) переменной находясь внутри локальной области видимости

#----------------------------------------------
# var = 100

# def increment():
#     global var
#     var += 1

# print(var)
# increment()
# print(var)
#----------------------------------------------
# def counter():
#     num = 0
    
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment
    

# c = counter() # <function counter.<locals>.increment at 0x7f93f0e2a050>

# print(c()) # 1
# print(c()) # 2
# print(c()) # 3
# print(c()) # 4
# print(c()) # 5
#----------------------------------------------
# print(dir(__builtins__))
# print(len(dir(__builtins__)))
#----------------------------------------------
# globals - func которая возвращает все имена в глобальной области видимости
# locals - func которая возвращает все имена в глобальной области видимости и локальной
#----------------------------------------------

def showStats(heroes, mobs):
    print(f'\nJohn Snow ты убил: \n\tЛанисстеров: {heroes}\n\tХодячих мертвецов: {mobs}\n\n')

def counter():
    num = 0
    
    def increment():
        nonlocal num
        num += 1
        return num
    return increment

count_kill_hero = counter()
count_kill_mob = counter()o
heroes = 0
mobs = 0

print('Приветствую тебя король севера John Snow!')

while True:
    print('Тебе доступны следующие действия:')
    print('1 - Убить героя\n2 - Убить моба\n3 - Посмотреть статистику\n4 - Выйти из игры\n')
    
    choice = int(input('Ваш выбор: '))
    
    if choice == 1:
        heroes = count_kill_hero()
        print('Вы обезглавили Ланистера!')
    elif choice == 2:
        mobs = count_kill_mob()
        print('Вы убили белого ходока!')
    elif choice == 3:
        showStats(heroes, mobs)
    elif choice == 4:
        print('Пока!')
        break
    else:
        print('Выбран неверный пункт меню!')        
#----------------------------------------------    
    
    