# print(1+1)
# a=1
# b=1
# print(a+b)

# import math
# print('math.sqrt(4)', math.sqrt(4))
# print('math.pow(4,2)', math.pow(4,2))

# import random
# print('random.random()', random.random())

# print('hello world')

# print('''
# hello
# world
# ''')


# print(len('hello world'*1000))
# print('hello world'.replace('world', 'universe'))

# students = ["egoing", "sori", "maru"]
# grades = [2,1,4]
# print(students[1])
# print(len(students))
# print(min(grades))

# import statistics
# print(statistics.mean(grades))

# import random
# print(random.choice(students))

# name= input('name:')
# message='hi, '+name+'... bye, '+name+'.'
# print(message)

# print(True)
# print(False)

# print(1==1)
# print(2==1)
# print(1!=1)

# print(1=1)

#012
# print(0)
# if True:
#     print(1)
# print(2)

# print('---')

# #02
# print(0)
# if False:
#     print(1)
# print(2)

# input_id = input('id:')
# id1 = 'egoing'
# id2 = 'basta'
# if input_id == id1:
#     print('welcome')
# elif input_id == id2:
#     print('welcome')
# else:
#     print('who?')

# input_id = input('id:')
# id = 'egoing'
# input_password = input('password:')
# password = '111111'
# if input_id == id:
#     if input_password == password:
#         print('welcome')
#     else: print('wrong password')
# else: 
#     print('Wrong id')



# print(0)
# if True:
#     print(1)
# else:
#     print(2)
# print(3)

# print(0)
# if False:
#     print(1)
# else:
#     print(2)
# print(3)

#014, if가 true기 때문
# print(0)
# if True:
#     print(1)
# elif True:
#     print(2)
# else:
#     print(3)
# print(4)

# #024
# print(0)
# if False:
#     print(1)
# elif True:
#     print(2)
# else:
#     print(3)
# print(4)

# #034
# print(0)
# if False:
#     print(1)
# elif False:
#     print(2)
# else:
#     print(3)
# print(4)


# names = ['egoing', 'sori', 'maru']
# for name in names: 
#     print('hi, '+name+' bye, '+name+'.')

# persons = [
#     ['egoing', 'seoul', 'web'],
#     ['basta', 'asan', 'iot'],
#     ['maru', 'seoul', 'ai'],
# ]

# # for person in persons:
# #     print(person[0]+', '+person[1]+', '+person[2])

# #위 코드를 간단하게 작성하면?
# for name, address, interest in persons:
#     print(name+', '+address+', '+interest)



# person =['egoing', 'seoul', 'web']
# name = person [0]
# address = person [1]
# interest = person [2]
# print(name, address, interest)

# name, address, interest = ['egoing', 'seoul', 'web']
# print(name, address, interest)


# person = {'name': 'egoing', 'address': 'seoul', 'interest': 'web'}

# for key in person:
#     print(key, person[key])

#위 dictionary를 list에 넣은 데이터

persons = [
    {'name': 'egoing', 'address': 'seoul', 'interest': 'web'},
    {'name': 'basta', 'address': 'asan', 'interest': 'iot'},
    {'name': 'maru', 'address': 'seoul', 'interest': 'ai'},
]

for person in persons:
    for key in person:
        print(key, person[key])