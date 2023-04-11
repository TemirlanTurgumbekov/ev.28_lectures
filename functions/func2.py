# string = 'Hello world! My name is John, last name is Snow. Nice to meet you!'

# def test(string):
#     result = string.split()[::-1]
#     return " ".join(result)

# print(test(string))

# def sum_of_args(a, b, c = 5, d = 5): # параметры
#     return a + b + c + d

# print(sum_of_args(1, 4, 5, 6)) # Аргументы

# res = sum_of_args

# print(res(5, 6, 7, 8))

# print(sum_of_args(5, 5))


# Позиционные и именнованные аргументы

# def printParams(a, b, c):
#     print(a, 'is stored in param a')
#     print(b, 'is stored in param b')
#     print(c, 'is stored in param c')
    
# printParams(1, 2, 3)
# printParams(c=5, b=15, a=10)

# def sum_of_args(a, b, c, d):
#     return a + b + c + d

# print(sum_of_args(5, 1, 5, 7)) # Arguments (позиционные аргументы)
# print(sum_of_args(a = 5, c = 20, b = 10, d = 15)) # KeyWordArguments (именованные аргументы)


# Оператор *
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [*a, *b]

# print(c)

#-----------------------------------------------
# *args, **kwargs в функциях

# def printScores(student, *args):
#     print(f'Name of student {student}')
    
#     print(f'AVG: {sum(args) / len(args)}')
    
#     for x in args:
#         print('Score:', x)
    
    
# printScores('John Snow', 100, 90, 99, 88)
#-----------------------------------------------
# def printPetNames(owner, **kwargs):
#     print(f'Owner name: {owner}')
#     # print(kwargs)
    
#     for pet, name in kwargs.items():
#         if type(name) == list:
#             print(f'{pet}:', *name)    
#         else:    
#             print(f'{pet}: {name}')

# printPetNames('John Snow', dog='Pluto', cat='Garflig', fish=['Nemo', 'Dory', 'Batya'], turtle = 'Leonardo')
#-----------------------------------------------
# def get_some_data(a, b, *args, **kwargs):
#     print('Параметры а и b:', a, b)
#     print('Аргументы:', args)
#     print('Именованные аргументы: ', kwargs)

# get_some_data(1, 2, 6,7,8,9,0, one = 1, two = 2, six = 6)

#-----------------------------------------------
# def generate_random_string(len_):
#     import string as s
#     import random
    
#     result = list(
#         random.choice(s.ascii_letters + s.digits) for i in range(0, len_)
#     ) + list(random.choice(s.punctuation))
#     random.shuffle(result)
#     return ''.join(result)

# print(generate_random_string(16))
#-----------------------------------------------

#-----------------------------------------------
# list_ = input().split(',')
# lis1 = list_.sort()
# print(lis1)
# print(list_)