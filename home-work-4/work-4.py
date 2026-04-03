## Списки:
1
worl_list = [1, 2, 3, 4, 5, 6]
worl_list.append(10)
worl_list.append(20)
worl_list.remove(10)
print(worl_list)

2
work_list = [2, 17, 24, 57, 21, 3]

sum_list = 0

for n in work_list:
    sum_list = n + sum_list

print(sum_list)

3
work_list_2 = [3, 12, 21, 32, 15, 37]

for n in work_list_2:
    print(n * 2)


## Кортежі:
1 
work_tuple = ('apple', 'banana', 'orange')
print(work_tuple[0])
print(work_tuple[1])
print(work_tuple[2])

2 
work_tuple_1 = (1, 2, 3, 4)
work_tuple_2 = (5, 6, 7, 8)
work_tuple_3 = work_tuple_1 + work_tuple_2
print(work_tuple_3)
 
## Словники:
1 
work_dict = {'name': 'Alexander', 'age': 35, 'sport': 'boxing', 'country': 'Ukraine'}
print(work_dict)

2
books_dict = {'Harry Potter': 1980, 'Game of Thrones': 2005, 'Predator': 1978}
books_dict['Predator 2'] = 1984
print(books_dict)

3
capitals_dict = {
    "United States": "Washington",
    "United Kingdom": "London",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo",
    "Canada": "Ottawa",
    "Australia": "Canberra",
    "Italy": "Rome",
    "Brazil": "Brasília",
    "South Korea": "Seoul",
    "Ukraine": "Kiyv"
}

user_country = "Ukraine"

if user_country in capitals_dict:
    print(capitals_dict[user_country])
else:
    print("Sorry, the name of this country is missing.")