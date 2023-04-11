# найти квадрат, куб, результат деления на 100 

# num1 = 5

# -> {'num':5, '2' : 25, '3': 125, '100': 0.5}

# num1 = 5
# num2 = 16
# num3 = 28
# num4 = 1154
# num5 = 31

# for i in range(1, 6):
#     num = int(input("Enter the number: "))

#     print({'num': num, '2': num ** 2, '3': num ** 3, '100': num / 100})
    
    
# RPY - don't repit yourself

# num1 = 5
# num2 = 16
# num3 = 28
# num4 = 1154
# num5 = 31

# def operations(num):
#     print({'num': num, '2': num ** 2, '3': num ** 3, '100': num / 100})
    

# operations(num1)
# operations(num2)
# operations(num3)
# operations(num4)
# operations(num5)

# Функция - это именнованая часть программы которая содержит в себе определенный набор инструкций
# и может вызываться в других частях программы столько раз сколько угодно

# def name_of_function(<a, b> #параметры):
    # <body> # код, какая-то логика которая булет давать конечный результат
    # <return> # оператор который помогаетвернуть результат

# name_of_func(5, 6 # аргументы)

# Параметры функции - это переменные которые будут принимать данные от пользователя и хранить в себе эти данные

# Аргументы функции- это данные которые мы передаем в функции в моменте вызова

# ls = [1, 2, 3, 4, 5]

# str1 = "hello world s vami kani i John Snow!"

# def our_len(obj):
#     i = 0
#     print(obj)
    
#     for x in obj:
#         i += 1
        
#     print(f'result: {i}')

# our_len(ls)
# our_len(str1)

# def isEven(obj):
#     if obj % 2 == 0:
#         return True
#     else:
#         return False


# print(isEven(5))   
# print(isEven(10))   
# print(isEven(15))



# def palindrom(words):
#     result = []
    
#     # for word in words:
#     #     if word.lower() == word[::-1].lower():
#     #         result.append(word)
    
#     # return result

#     return [i for i in words if i.lower() == i[::-1].lower()]
            

# ls = ['tima', 'tiit', 'Ono', 'ghbdtn', 'dovod', 'kazak']
# print(palindrom(ls))


# def get_depozit(money, period):
#     if money < 30000:
#         raise ValueError('Вложить можно более 30000')
    
#     if period < 3:
#         raise ValueError('Период должен быть более 3 лет')
    
#     year = 0
#     while year < period:
#         money += money * 0.1
#         year += 1
        
#     return money

# try:
#     money = float(input("Введите сумму вложения: "))
#     year = int(input("Введите сумму вложения: "))
#     print(get_depozit(money, year))
# except ValueError as e:
#     print(e)

# def test_func(first, last, step):
#     pass

