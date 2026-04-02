# Умовні конструкції:
#1
password = 'password123'

if password == 'password123':
    print("Ви увійшли в систему")
else:
    print("Неправильний пароль")

#2
day_of_week = {1 : 'Monday', 2 : 'Tuesday', 3 : 'Wednesday', 4 : 'Thursday', 5 : 'Friday', 6 : 'Saturday', 7 : 'Sunday'}

num_of_day = 6

if num_of_day in day_of_week:
    print(day_of_week[num_of_day])
else:
    print('Wrong number of day')

#1
num = 0
number = 6

while num < 10:
    num += 1
    print(f'{number} * {num} = {number * num}')
    
#2
test_list = [2, 14, 12, 25, 43]
total_sum = 0

for n in test_list:
    total_sum += n

print(total_sum)

#3
num = 8
factorial = 1

while num > 1:
    factorial = factorial * num 
    num -= 1

print(factorial)

#4
n = 1

while n <= 50:
    if(n % 2 == 0): 
        print(n)
    n += 1

#5
num = 2

while num <= 50:
    is_prime = True
    divisor = 2  
    
    while divisor < num:
        if num % divisor == 0:
            is_prime = False
            break 
        divisor += 1  
        
    if is_prime:
        print(num)
        
    num += 1
    


