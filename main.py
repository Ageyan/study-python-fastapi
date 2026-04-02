# LESSON 2 ------------------------------------------------

# name = "Tom"
# Name = 'Jim'
# print(name, Name)

# user_email = 'example@gmail.com'
# userEmail = 'example@gmail.com2'
# print(user_email, userEmail)

# name = 'Jon'
# print(name)
# name = 'Tom'
# print(name)

# num1 = 100
# num2 = 10 
# num_3 = num1 + num2
# num_4 = num1 - num2
# num_5 = num1 * num2
# num_6 = num1 / num2
# print(num_3, num_4, num_5, num_6)

# num_1 = 7
# num_2 = 2 

# num_3 = num_1 / num_2
# num_4 = num_1 // num_2
# num_5 = num_1 % num_2
# print(num_3, num_4, num_5)

#######################################################   Оператори порівняння and/or/in/not in

# num = 10
# name = 'Tim'
# result = num > 5 and name == 'Tim' # and - показує true коли всі умови вірні 
# result2 = num < 5 or name == 'Tim' # or - показує true коли хоча б одна умова вірна  
# print(result, result2)

# name = 'Tom'
# message = 'Tom got some money'
# print(name in message) # in - перевіряє чи є змінная у іншій змінній 
# print(name not in message) # not in - перевіряє чи немає 

# age = 50 
# name = 'Joe'
# animal = 'cat'
# print(age == 50 and 'J' in name and animal != 'dog')

#######################################################   Типи даних 
# num_1 = 5 
# print(type(num_1))

# dct = {'name' : 'Jon', 'age' : 23}
# print(type(dct))

# lst = [1, 2, 3, 4, 5]
# dct = {'name' : 'Tom', 'age' : 5}
# name = 'Tom'
# tpl = {'n', 'a', 'g'}

# result = dct['age'] in lst and name in dct['name']
# print(result)

####################################################### Вбудовані функції для роботи с типами даних 

# num_1 = '1'
# print(type(num_1)) #str
# num_1 = int(num_1)
# print(type(num_1)) #int

# string = 'Hello world!'
# print(len(string)) 
# string = string.upper() # ASDGFG
# print(string)
# string = string.lower() # sdfasdf
# print(string)
# string = string.capitalize() # Tdfdfg
# print(string)
# string = string.replace('!', '?')
# print(string)
# string = string.split()
# print(string)
# string = " ".join(string)
# print(string)
# string = string.count('o')
# print(string)
# string = 1
# string = str(string)
# print(type(string))

# base_list = [1, 2, 3]
# print(len(base_list))
# base_list.append(4)
# print(base_list)
# base_list.extend([5, 6, 7])
# print(base_list)
# print(base_list.index(4))


# base_dict = {'name' : 'Tom', 'age' : 40, 'height' : 180}
# print(base_dict.keys())
# print(base_dict.values())
# print(base_dict.items())
# print(base_dict['name'], base_dict.get('name'))
# print(base_dict['name'], base_dict.get('is_animal', 'No')) # get можна передати друге значення яке повернеться у випадку, якщо ключа не існує 

# LESSON 3 ------------------------------------------------ IF/ELSE/ELIF
#
#string = 'Hello world!'

#if 'Hello' not in string: 
#    print('Hello in string')
#elif 'world' in string:
#    print('world in string')
#else:
#    print('World not in string')
#

# a = 10 
# b = 20

# if a == 11 or b < 30:
#     print(a + b)
# else: 
#     print('Wrong condition')

# test_list = ['hello', 'test', 1, 2, 3]

# if 'hello' in test_list and 1 in test_list:
#     print('Hello 1')
# elif 'test' in test_list and 4 not in test_list:
#     print('Test not 4')
# else:
#     print('Your conditions were wrong')

# a = 10 
# b = 20 
# c = 'chat is active'
# d = 'count of users'

# if len(c) >= b:
#     print(c)
# elif len(d) <= a:
#     print(d)
# else:
#     print('wrong')

# user_1 = {
#     'name': 'Tom',
#     'age': 21, 
#     'balance': 20000,
#     'curencu': 'USD',
#     'status': True
# }

# user_2 = {
#     'name': 'John',
#     'age': 17, 
#     'balance': 5000,
#     'curencu': 'EUR',
#     'status': False
# }

# user_3 = {
#     'name': 'Karina',
#     'age': 30, 
#     'balance': 100000,
#     'curencu': 'UAH',
#     'status': True
# }

# list_of_currency = ['USD', 'GBR', 'UAH', 'EUR']

# if user_1['name'] and user_1['age'] >= 18 and user_1['status']:
#     if user_1['balance'] >= 10000 and user_1['curencu'] in list_of_currency:
#         print(f"Hello! you can create your binance account, welcome {user_1['name']}")
#     elif user_1['balance'] >= 1000 and user_1['curencu'] in list_of_currency:
#         print('Your need more money')
#     else:
#         print('Money critical not enougth')
# elif not user_1['name']:
#     print('Please, write your name in your account description')
# elif user_1['age'] < 18:
#     print('For registry binance account you have to be 18 year old')
# else: 
#     print('Something went wrong!')

#------------------------------------------------ WHILE/FOR 

# test_list = [1, 2, 3, 4, 5]

# a = 0 

# while a < 10:
#     print(a)
#     a += 1
    
# while len(test_list) < 10:
#     test_list.append(3)
#     print(test_list)

# test_list = ['test', 'python', 'code']

# for s in test_list: 
#     if s == 'test':
#         print(s)
#     elif s == 'python':
#         print(s)
#     else:
#         print(s)


# a = 0
# add_list = []

# while len(add_list) < 10:
#     print('Len of list:', len(add_list))
#     add_list.append(a)
#     a += 1
#     if len(add_list) == 5:
#         print('You are at middle of list')

# user_1 = {
#     'user_name': 'tester',
#     'role': 'admin',
#     'account_connection': True
# }

# user_2 = {
#     'user_name': 'junior',
#     'role': 'user',
#     'account_connection': False
# }

# user_3 = {
#     'user_name': 'middle',
#     'role': 'user',
#     'account_connection': True
# }

# list_of_users = [user_1, user_2, user_3]

# for user in list_of_users:
#     print(f"Work with {user['user_name']} account <-------------")
#     if not user['account_connection']:
#         count_of_tries = 10
#         while count_of_tries != 0:
#             if count_of_tries == 5:
#                 user['account_connection'] = True
#                 break
#             print('Try to connect to user account')
#             count_of_tries -= 1
#             print('Count of trise left: ', count_of_tries)
#     elif user['role'] == 'admin':
#         print(f'Hello in system {user["user_name"]}')
#     else: 
#         print('Welcome on the board')

# print('All users were checked!')