
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
        

#################################rWhile lops################################################# 

sentence = input('Please type in a word:')
s = []
while True:
    
    if sentence == 'end' :
        break
    s.append(sentence)
    sentence = input('Please type in a word:')
    if sentence == s[-1]:
        break

print(' '.join(s))  



#################################rWhile lops################################################# 

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




#################################While lops################################################# 

 
count = 2 
while count >=2 and count <=30:
    if count % 2 == 0:
        print(count)
    count = count +1


#################################While lops################################################# 
 # Fix the program
print("Are you ready?")
number = int(input("Please type in a number: "))
while number > 0:
    print(number)
    number = number - 1
    
print("Now!")

#################################While lops################################################# 
 # Fix the program

number = int(input("Please type in a number: "))

v= 1 

while v <= number:
    print(v)
    
    v = v * 2
     

#################################While lops################################################# 
 # Fix the program
number = int(input("Upper limit:"))

v= 1 
base = int(input('Base:'))
while v <= number:
    print(v)
    
    v = v * base


#################################While lops################################################# 

limit = int(input("Limit:"))
n= 1
m = 0 
while m < limit:
    print(n)
    m = m + n
    n = n + 1
print(m)


#################################While lops################################################# 


limit = int(input("Limit:")) #2
num = 1
a = 0 
l = [] 


while a < limit:
    l.append(str(num))
    x = ' + '.join(l)
    a = a + num
    num = num + 1

print(f'The consecutive sum: {x} = {a}')


#################################Working with strings ################################################# 

n = 10 
row = "^"

while n> 0 :
    
    print(n*" " + row )         # this line prints the spaces plus the symbols. the space start a 10 and goes down to one
    n= n -1
    row = row + "^^"


########################################################################################

s = input("Please type in a string:")
a = int(input("Please type in an amount:"))

print(a*s)


########################################################################################
stringa = input("Please type in string 1:")
stringb = input("Please type in string 2:")
if len(stringa) > len(stringb):
    print(f"{stringa} is longer")
elif len(stringa) < len(stringb):
    print(f"{stringb} is longer")
else:
    print("The strings are equally long")

########################################################################################

letter = input("Enter letter ")
c = 0
d = -1 
while len(letter) > c:
    print(letter[d])
    
    d = d -1
    c = c+1


########################################################################################
string1 = input("Please type in a string: ")


if string1[-2] != string1[1]:
    print("The second and the second to last characters are different")
elif string1[-2] == string1[1]:
    print(f"The second and the second to last characters are {string1[1]}")
''
########################################################################################

w = int(input("With:"))
h = "#"
print(h*w)


########################################################################################
w = int(input("With:"))
hei = int(input("Height:"))
h = "#"

ancho = h*w

for x in range(0,hei):
    x = ancho
    print(x)

########################################################################################



w = "-"
while True: 
    letter = input("Please type in a string: ")
    print(letter)
    print(w *len(letter))
    if letter == "":
        break

########################################################################################
#option 1
s = input("Please type in a string:")
c = len(s)
v = "*"
if c < 20:
    k = (c - 20)*(-1)

    print(f"{k*v}{s}")
else:
    print("nope")
    
#option 2
s = input("Please type in a string:")
st = (len(s) - 20)* (-1)
star = '*'*st
print(f"{star}{s}")

#option 3

s = input("Please type in a string:")
n = 20
b= "*"
while len(s)< n: #dos
    
    n= n- len(s)
    if n + len(s) == 20:
        
        break
print(f"{b*n}{s}" )      
    
'''        
    
#######################################################################################

c = input("Word: ")
n= 30
side = n-29
d = int(n-2)/2
k = "* "
b=""

print(f"{k*n}")
print(f"{side}{b*d}{c}{b*d}{side}")
print(f"{k*n}")
