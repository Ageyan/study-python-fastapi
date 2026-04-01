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