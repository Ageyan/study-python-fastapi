#1
name = 'Andrey'
message = 'Andrey go to work'
age = 30 
height = 181.5
is_man = True
car = ['Audi', 'Sckoda', 'Buick']
user_data = {'id' : 1, 'name' : 'Andrey'}
base_tuple = (1, 2, 30, 4, 180)
user_none = None

#2
result = age < height and height == age + 151.5
result_2 = age == height or name != height
result_3 = name in message
result_4 = age in base_tuple
result_5 = height not in base_tuple
result_6 = is_man is not user_none

#print(result, result_2, result_3, result_4, result_5, result_6)

#3 
# print(type(name))
# print(type(age))
# print(len(message))
# print(name.capitalize(), name.upper(), name.lower())
# print(message.replace('work', 'shop'))
# message_split = message.split()
# print(message_split)
# message_join = ' '.join(message_split)
# print(message_join)
# print(message.count('o'))
# print(type(str(age)))

#print(len(car))
#car.append('BMW')
#print(car)
#car.extend(['Suzuki', 'Mercedes', 'Porshe'])
#print(car)
#print(car.index('Sckoda'))
#print(car[4])

#user_data = {'id' : 1, 'name' : 'Andrey'}
#print(user_data.keys())
#print(user_data.values())
#print(user_data.items())
#print(user_data['id'], user_data.get('is_man', 'No'))

#4
num_str = 125 
num_str_1 = str(num_str)
print(type(num_str_1))

message = 'Hi, my name is Python!'
print(message.replace('y', '0').replace('i', '1'))

split_test = 'This is a split test'
split_test_2 = split_test.split()
print(split_test_2)
split_join = ' '.join(split_test_2)
print(split_join)
print(len(split_join))

list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)
print(list_append)
list_extend = [4, 5, 6]
list_extend_2 = [7, 8, 9]
list_extend.extend(list_extend_2)
print(list_extend)
print(list_extend.index(6))
print(len(list_append))

dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(dict_test['car'])
print(dict_test['where'])
print(dict_test.keys())
print(dict_test.values())
print(dict_test.items())