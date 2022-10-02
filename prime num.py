range = int(input('Enter the number range to find prime number :'))
number = 1
while number < range:
    if number % 2 == 0:        
     print(number," is Not Prime Number")
    else:
     print(number," is Prime Number")
    number += 1