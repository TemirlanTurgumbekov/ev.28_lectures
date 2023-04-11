'''
Встроенные функции
'''

# Анонимная функция - lambda (Обычная функция с одной особенностью, у нее нет имени) Принимает сколько угодно параметров

# def hello():
#     return 'Hello'

# x = lambda: 'hello'

# print(x())

# x = lambda a, b, c:  (a * b) % c

# print(x(5, 5, 5))

# x = lambda a, b, c=1: (a * b) ** c

# print(x(1, 2))

# def myFunc(n):
#     return lambda num: num * n

# my_dobler = myFunc()

# print(my_dobler(50))

# dict_ = {
#     'John': 500,
#     'Tirion': 160_000,
#     'Sanchar': 20,
#     'Ayana': 100_000,
# }


# new_dict = dict(sorted(dict_.items(), key=lambda x:x[1], reverse=True))

# print(new_dict)
'''
map(function, iterable) - принимает к каждому элементу внутри iterable функцию, которую мы ей передаем в function, закидывая в результат те данные, которые возвращают функция. В результате сы получаем mapobject(iterable), в котором хранятся все наши данные
'''

# ls = ['one', 'two', 'three', 'four']

# new_list = list(map(lambda x: x.capitalize(), ls))

# print(new_list)


# from simple_term_menu import TerminalMenu

# menu = TerminalMenu(['1. Войти', '2. Регистрация', '3. Забыли пароль?', '4. Выйти'])
# menu.show()

# names = ['Tima', 'Oleg', 'Mayones']

# new_list = list(map(lambda x: f'hello, mr//mrs {x}', names))

# print(new_list)


# Функция высшего порядка - функция, которая принимает в качестве аргумента другую функцию



# filter(function, itereble) - применяет ко всем элементам iterable функцию, которую мы передали и возвращает filterobject(итератор) только с теми элементами, для которых функция вернула True

# ls = ['one', 'lili', 'oleg', 'billi', 'tirion']

# new_list = list(filter(lambda x: len(x) > 4, ls))

# print(new_list)

# # enumerate(iterable) - пронумеровывает каждый элемент внутри iterable ее собственным индексом

# ls = ['str1', 'str2', 'str3']

# new_list = list(enumerate(ls))

# print(new_list)

# zip(iterables) - она соединяет каждый элемент итерируемых объектов между собой в тип данных tuple и возвращает итератор

# ls1 = [1,2,3]
# ls2 = [100, 200, 300]

# result = list(zip(ls1, ls2))

# print(result)


# ls1 = [1,2,3, 4, 5]
# ls2 = [100, 200, 300, 400, 500, 600]
# ls3 = [10, 20, 30]

# result = list(zip(ls1, ls2, ls3))

# print(result)

# zip - для создания словарей
# d_keys = ['hostname', 'location', 'vendor', 'model', 'IP']

# data = {
#     'oktbr': ['biskek_oktbr', 'Gorkaya 212', 'Vefa', 'Cisco', '10.255.0.12'],
#     '1may': ['biskek_may', 'Jibel-Jolu', 'Belyi', 'Cisco', '11.251.1.11'],
#     'svrl': ['biskek_svrl', 'Ahunbaeva 211', 'TC', 'Cisco', '11.251.104.9'],
# }

# bishkek_data = {}

# for k in data:
#     bishkek_data[k] = dict(zip(d_keys, data[k]))
    
# print(bishkek_data)

# -------------------------------------------------
# all(), any()

# all(Iterable) - Возвращает True, если все итерируемого объекта истины, иначе возвращает False
# ls = [5, 6, 7]

# print(all(ls)) -> True
# ip = '10.255.155'

# str_ = ip.split('.')

# print(str_)
# if len(str_) != 4:
#     print('No')
    
# else:
#     print('Yes')

# -------------------------------------------------
# any - Возвращает True, если хотя бы один элемент истина

# ignore = ['rm-rf', 'sudo', 'reset', 'poweroff']

# command = input('Enter your command: ').split(' ')
# if any():
#     raise Exception('Block you!')

# print('It\'s Ok!')

# -------------------------------------------------

# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
# 'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
# 'Nik': {'history': 84, 'math': 85, 'literature': 87}}

# res = {}
# for key, value in dict_.items():
#     for inner_key, inner_value in value.items():
#         if max(value.values()) == inner_value:
#             res[key] = inner_key

# print(res)



# new_dict = {}
# for key, value in dict_.items():
#     new_dict = {inner_key: inner_value for inner_key, inner_value in value.items() if max(value.values()) == inner_value}
# print(new_dict)

# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
# 'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
# 'Nik': {'history': 84, 'math': 85, 'literature': 87}}

# new_dict={x:max(y,key=lambda x:y.get(x)) for x,y in dict_.items()} 
# print(new_dict)




# -------------------------------------------------
# from random import choices
# from string import ascii_letters, digits
# from itertools import repeat
# import os 

# symbols = '_()+-@!#%'
# q_pass = int(input('Enter count of passwords: '))

# result = {
#     f(choices(ascii_letters, k=15), choices(digits, k=6), choices(symbols, k=2)) for f in repeat(lambda x, y, z: ''.join(set(x+y+z)), q_pass)
# }

# for i, j in enumerate(result):
#     print(f'Password №{i + 1}: {j}')

# input()
# os.system('cls||clear')    
# print(f'Count of password: {len(result)}')
# input()
# os.system('cls||clear')    
# -------------------------------------------------
# -------------------------------------------------

# nums = [-2,-1,-1,1,2,3]

# count_neg = 0
# count_pol = 0

# for i in nums:
#     if i > 0:
#         count_pol += 1
#     elif i < 0:
#         count_neg +=1
        
# return count_neg if count_neg > count_pol else count_pol

# nums = [4,1,2,3]
# nums1 = sorted(nums[::2])
# nums2 = sorted(nums[1::2], reverse=True)

# temp = list(zip(nums1, nums2))

# res = []
# for i in temp:
#     res.extend(i)
# print(res)
# tuple_ = (1, 2, 3, [1, 2,3])
# print(tuple_)

# tuple_[3].append(4)
# print(tuple_)



# def func15(users):
#     for i in users:
#         if 'IT' in i['work']:
#             print(f"{i['name']}, скидки в магазине компьютерной техники!")


# users = [
#   { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer' },
#   { 'name': 'Helen', 'age': 35, 'work': 'Nurse' },
#   { 'name': 'Bob', 'age': 35, 'work': 'Driver' },
#   { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer' },
#   { 'name': 'Helga', 'age': 35, 'work': 'IT-HR' }
# ]

# func15(users)

