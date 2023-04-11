# list comprehensions - генераторы списков
'''list comprehensions - упрощенный подход к созданию списков,
который задействует цикл for, а так же конструкцию if 
для определения того, что в итоге попадет в наш список

'''

#list -> 0 - 200 -> num % 2 == 0

'''ls = []

for x in range(0, 201):
    if x % 2 == 0:
        ls.append(x)
        
print(ls)

'''

# ls = [x for x in range(0, 301) if (x % 2 != 0) and (x % 3 == 0)]
# print(ls)

# ls = []

# for x in range(0, 101):
#     if x % 2 == 0:
#         ls.append(x ** 2)
#     elif x % 3 == 0:
#         ls.append(x ** 3)

# print(ls)

# ls = [x ** 2 if x % 2 == 0 else x ** 3 for x in range(0, 101) if x % 2 == 0 or x % 3 == 0]
# print(ls)

#-----------------------------------
# new_list = [expression for item in itereble <if condition == True>]

# ls = [str(i * 2) for i in range(0, 11)]
# print(ls)

# ls = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# # result = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ls1 = [item for x in ls for item in x]
# print(ls1)

#----------------------------------------

# from datetime import datetime

# start = datetime.now() # 19:54

# # ls = []
# # for x in range(0, 100_000_000):
# #     ls.append(x)
# ls = [x for x in range(0, 100_000_000)]

# finish = datetime.now()

# res = finish - start

# print(res)

#----------------------------------------
# set compehensions
# set_ = {x for x in range(1, 100)}

# print(set_, type(set_))


#----------------------------------------
#dict compehensions
# dick = {
#     "key": "value"
#     .......
#     .......
# }
# dict_ = {x: x ** 2 for x in range(0, 16)}
# print(dict_)

#----------------------------------------
# names = ['John', 'Tirion', 'Eygan', 'Sansa', 'Ramsi']

# dict_= {name: len(name) for name in names}

# print(dict_)

#----------------------------------------
dict1 = {
    'Soke': {'history': 99, 'fizyk': 95, 'math': 94},
    'Omoke': {'history': 84, 'fizyk': 68, 'math': 100},
    'John': {'history': 101, 'fizyk': 87, 'math': 90},
}

# dict2 {name: subject for name in dict1.keys()}

# res = {}
# for key, value in dict1.items():
#     for inner_key, inner_value in value.items():
#         if max(value.values()) == inner_value:
#             res[key] = inner_key

#----------------------------------------

res = {
    key: inner_key for key, value in dict1.items()
        for inner_key, inner_value in value.items()
            if inner_value == max(value.values())}
print(res)

theBestStudent = ""

for key, value in res.items():
    if(max(res.values()) == value):
        theBestStudent = key

print(theBestStudent)
