'''
mean = 0
add = 0
numbers = 0
p = 0
n = 0 
print('Please type in integer numbers. Type in 0 to finish.') 
while True:
    
    number = int(input("Number:"))
    if number == 0:
        break
    numbers = numbers +1
    add = add + number
    mean = add / numbers
    if number >=0:
        p = p +1
    elif number < 0 : 
        n= n +1 




print(f'Numbers typed in {numbers}')
print(f'The sum of the numbers is {add}')
print(f'The mean of the numbers is {mean}')
print(f'Positive numbers {p}')
print(f'Negative numbers {n}')

              
'''
w = input('Word: ')
c = (len(w)-30)*(-1)
 
if c % 2 ==0:
    l = (c//2)*"*"
    print("*"*30)
    print(f"{l}{w}{l}")
    print("*"*30)
elif c % 2!=0:
    e =" "
    f = (c//2)*"*"
    fk= len(f)*"*"+"*"
    print("*"*30)
    
    print(f"{fk}{w}{f}")
    print("*"*30)

if len(l) > 0 :
    for x in range(1,len(l))