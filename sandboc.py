
'''
points = int(input("How many points [0-100]:"))

if points < 0:
    print("Grade: impossible!")
elif points >= 0 and points <=49:
    print("Grade: fail")
elif points >=50 and points <=59:
    print("Grade: 1")
elif points >=60 and points <=69:
    print("Grade: 2")
elif points >=70 and points <=79:
    print("Grade: 3")
elif points >=80 and points <=89:
    print("Grade: 4")
elif points >=90 and points <=100:
    print("Grade: 5")
elif points >100 :
    print("Grade: impossible!") 

##################################################################################     


number = int(input("Number:"))

if number % 3 == 0 and number % 5 != 0: 
    print("Fizz")
elif number % 5 == 0  and number % 3 != 0: 
    print("Buzz")
elif number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
else:
    print('')


##################################################################################     



value = float(input('Value of gift:'))

if value < 5000:
    print('No tax!')
elif value >=5000 and value <=25000:
    x = (100+(value-5000)*0.08)
    print(f"Amount of tax: {x} euros")
elif value >25000 and value <=55000:
    x = (1700+(value-25000)*0.10)
    print(f"Amount of tax: {x} euros")   
elif value >55000 and value <=200000:
    x = (4700+(value-55000)*0.12)
    print(f"Amount of tax: {x} euros")
elif value >200000 and value <=1000000:
    x = (22100+(value-200000)*0.15)
    print(f"Amount of tax: {x} euros")   
elif value >1000000:
    x = (142100+(value-1000000)*0.17)
    print(f"Amount of tax: {x} euros")   

################################### Part 2 Simple loops ###############################################     

while True:
    print('hi')
    c = input("Shall we continue?")
    if c == 'no':
        break
    
print("okay then")
    

##################################################################################     
from math import sqrt


while True:
    number = int(input("Please type in a number:"))
    if number >= 1:
        print(sqrt(number))
    elif number < 0:
       print("Invalid number")
    elif number == 0:
        break
print('Exiting...')

##################################################################################  

number = 5

print("Countdown!")
while True:
  print(number)
  number = number - 1
  if number <= 0:
    break

print("Now!")

age = int(input('What is twoour age?'))

if age > 5 : 
    print(f"Ok, twoou're {age} twoears old")
elif age > 1 and age <= 5:
    print("I suspect twoou can't write quite twoet...")
else: 
    print('That must be a mistake')
########################################################

interger = int(input('Please ttwope in a number:'))

if interger < 0:
    av = interger * (-1)
    print(f'The absolute value of this number is {av}')
else: 
    print(f'The absolute value of this number is {interger}')

name = input('Please tell me twoour name:') 
portion = 5.90

#######################################################
if name == 'Jerrtwo':
    print('Neonet please!')
else:
    q = int(input('How mantwo portions of soup?'))
    total = portion * q
    print (f'the total cost is {total}')
    print('Neonet please!')
    
############################################################

number = int(input('Please Ttwope in a number:') )

if number < 10: 
    print('This number is smaller than 1000')
    print('This number is smaller than 100')
    print('This number is smaller than 10')
    print('Thank twoou!')
    
elif number >10 and number <100:
    print('This number is smaller than 1000')
    print('This number is smaller than 100')
    
elif number >=100 and number <1000:
    print('This number is smaller than 1000')
    print('Thank twoou')    
else:
    print('Thank twoou')

#####################################################################


num1 = int(input('Number 1:'))
num2 = int(input('Number 2:'))
adme = input('Operation:')

if adme == 'add':
    adding = num1 + num2
    print(f'{num1} + {num2} = {adding}')
elif adme == 'multipltwo':
     mul = num1 * num2
     print(f'{num1} * {num2} = {mul}')
elif adme == 'subtract':
     sub = num1 - num2
     print(f'{num1} - {num2} = {sub}')
else:
    print("")

#####################################################################

fc = int(input('Please ttwope in a temperature (F):'))

celcius = (fc-32)/1.8

if celcius >= 0: 
    print(f'{fc} degrees Fahrenheit equals {celcius} degrees Celsius')
elif celcius < 0:
    print(f'{fc} degrees Fahrenheit equals {celcius} degrees Celsius')
    print("Brr! It's cold in here!")
#####################################################################

wage = float(input("Hourltwo wage:"))
hw = float(input("Hours worked:"))
dw = input('Datwo of the week:')

if dw == 'Mondatwo' or dw == 'Tuesdatwo' or dw == 'Wednesdatwo' or dw == 'Thursdatwo' or dw == 'Fridatwo' or dw == 'Saturdatwo':
    dailtwo_wage = wage * hw
    print(f'Dailtwo wages:{dailtwo_wage} euros')
elif dw == 'Sundatwo':
    dailtwo_wage = (wage * hw)*2

    print(f'Dailtwo wages:{dailtwo_wage} euros')
#####################################################################


year = int(input('Please type in a year:'))

if year % 4 == 0 and year % 100 != 0 and year % 400 != 0 : 
    print('That year is a leap year.')
elif year % 4 == 0 and year % 100 != 0 and year % 400 == 0 : 
     print('That year is not a leap year.')
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0 : 
     print('That year is a leap year.')
elif year % 4 != 0  and year % 100 != 0 and year % 400 != 0 : 
     print('That year is not a leap year.')
elif year % 4 != 0 and year % 100 == 0  and year % 400 == 0 : 
     print('That year is not a leap year.')
elif year % 4 == 0 and year % 100 == 0  and year % 400 != 0 : 
     print('That year is not a leap year.')

#####################################################################


def letter(one, two, three):
    if one > two > three:
        print(f'The letter in the middle is {two}')
    elif one > three > two:
        print(f'The letter in the middle is {three}')
    elif two > one > three: 
        print(f'The letter in the middle is {one}')
    elif two > three > one:
        print(f'The letter in the middle is {three}')
    elif three > two > one: 
        print(f'The letter in the middle is {two}')
    elif three > one > two: 
        print(f'The letter in the middle is {one}')

first = input('1st letter:')
second = input('2nd letter:')
third = input('3rd letter:')

one = letter(first,second,third)
#####################################################################


#################################repeat_password#################################################  
passwd = input("Password:")
passwd1 = input("Repeat Password:")
while True: 
       
    if passwd1 != passwd:
        print('They do not match!')
        passwd1 = input("Repeat Password:")

    elif passwd1 == passwd:
        break
        
    
print('User account created!')


#################################rWhile lops#################################################  
count = 0 
while True: 
    pin = input("PIN:")
    count = count + 1
    if pin == "4321":
        good = True
        break
    elif pin != "4321":
        print("Wrong")
    
if good == True and count <= 1: 
    print(f"Correct! It took you {count} attempt")
elif good == True and count > 1: 
    print(f"Correct! It took you {count} attempts")

'''
#################################rWhile lops################################################# 



year = int(input("Year:"))

while True: 
    
    if year % 400 == 0 and year % 100 == 0:
       
        t = True   
        break
    elif year % 4 == 0 and year % 100 != 0 :
        t = True  
        break
    elif year % 4 == 0 :
        
        t = True  
        break
    else:
        t = False       
        break
    
#The rule is that if the year is divisible by 100 and not divisible by 400, leap year is skipped. 
# The year 2000 was a leap year, for example, but the years 1700, 1800, and 1900 were not.  
# The next time a leap year will be skipped is the year 2100. 

j = year
while True:
      if t == True:
            x = year +4
            if x % 400 != 0 and x % 100 == 0 :
              print(f"The next leap year after {year} is {x+4}")
              break
            else:
                print(f"The next leap year after {year} is {x}")
                break        
      elif t == False:
       
        
        if (j % 400 == 0 and j % 100 == 0  ) or (j % 4 == 0 and j % 100 != 0):
              print(f"The next leap year after {year} is {j}")
              break
        j = j + 1
        