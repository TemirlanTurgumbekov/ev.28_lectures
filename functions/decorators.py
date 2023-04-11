# Декораторы - это функция которая позволяет без изменений кода функции расширить ее функционал
# ------------------------------------------------

# Пример декоратора
# def decorator(func):
#     print(func)
#     func()

# def hello():
#     print('Hello stranger!')

# def john():
#     print('My name is John Snow! I\'m King of North')
    
# decorator(hello)
# print('!!!!!!!!!!!!!!!!!!!')
# decorator(john)
# ------------------------------------------------
# pythonic way -> @
# Синтаксический сахар

# def decorator(func):
#     def wrapper():
#         print(f"Мы вызвали функцию {func.__name__}")
#         func()
#     return wrapper


# @decorator  # @decorator -> decorator(hello)
# def john():
#     print('My name is John Snow! I\'m King of North')

# @decorator    
# def hello():
#     print('Hello stranger!')
    
# hello()
# print('-----------------------------')
# john()
# ------------------------------------------------

# def benchmark(func):
#     def wrapper(*args, **kwargs):
#         import time
#         start = time.time()
#         func()
#         finish = time.time()
#         print(f'Время выполнения функции: {func.__name__}\nФункция отработала за: {finish - start}')
#     return wrapper

# @benchmark
# def loop():
#     i = 0
#     range_number = 100_000
    
#     while i < range_number:
#         i += 1

# @benchmark
# def add():
#     i = 0
#     ls = []
#     range_number = 100_000
    
#     while i < range_number:
#         ls.append(i)
#         i += 1
#     print(ls)

# add()
# loop()
# ------------------------------------------------
# def bold(func):
#     def wrapper(*args, **kwargs):
#         res = '<bold>' + func(*args, **kwargs) + '</bold>'
#         return res
#     return wrapper

# def div(func):
#     def wrapper(*args, **kwargs):
#         res = '<div>' + func(*args, **kwargs) + '</div>'
#         return res
#     return wrapper

# @div
# @bold
# def str_(name):
#     return name

# print(str_('John Snow'))
# ------------------------------------------------
# def trace(func):
#     def wrapper(*args, **kwargs):
#         print(f'Trace: вызвана {func.__name__}(), она приняла \nargs:{args} \nkwargs: {kwargs}')
#         original_result = func(*args, **kwargs)
#         print(f'Trace: вызвана {func.__name__}(), она вернула: {original_result}')
#         return original_result
    
#     return wrapper

# @trace
# def say(name, address):
#     return f'{name} --> {address}'

# @trace
# def hello(name, last_name, country):
#     return f'Hello {name} {last_name}, from {country}'

# say('Tima', 'Bakery street 221B')
# print('__________________________________')
# hello('Tima', 'Ahumbaev', country='Canada')
# ------------------------------------------------

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
merge_from = input()
merge_to = input()

new_list = []
for i in chars:
    if i == merge_from:
        for j in chars[i:]:
            new_list.append(j)
            if j == merge_to:
                break
        break

new_list += chars[chars.index(merge_to):]
    

print(new_list)