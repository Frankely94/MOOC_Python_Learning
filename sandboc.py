
'''
points = int(input("How many points [0-100]:"))

if points < 0:
    #print("Grade: impossible!")
elif points >= 0 and points <=49:
    #print("Grade: fail")
elif points >=50 and points <=59:
    #print("Grade: 1")
elif points >=60 and points <=69:
    #print("Grade: 2")
elif points >=70 and points <=79:
    #print("Grade: 3")
elif points >=80 and points <=89:
    #print("Grade: 4")
elif points >=90 and points <=100:
    #print("Grade: 5")
elif points >100 :
    #print("Grade: impossible!") 

##################################################################################     


number = int(input("Number:"))

if number % 3 == 0 and number % 5 != 0: 
    #print("Fizz")
elif number % 5 == 0  and number % 3 != 0: 
    #print("Buzz")
elif number % 3 == 0 and number % 5 == 0:
    #print("FizzBuzz")
else:
    #print('')


##################################################################################     



value = float(input('Value of gift:'))

if value < 5000:
    #print('No tax!')
elif value >=5000 and value <=25000:
    x = (100+(value-5000)*0.08)
    #print(f"Amount of tax: {x} euros")
elif value >25000 and value <=55000:
    x = (1700+(value-25000)*0.10)
    #print(f"Amount of tax: {x} euros")   
elif value >55000 and value <=200000:
    x = (4700+(value-55000)*0.12)
    #print(f"Amount of tax: {x} euros")
elif value >200000 and value <=1000000:
    x = (22100+(value-200000)*0.15)
    #print(f"Amount of tax: {x} euros")   
elif value >1000000:
    x = (142100+(value-1000000)*0.17)
    #print(f"Amount of tax: {x} euros")   

################################### Part 2 Simple loops ###############################################     

while True:
    #print('hi')
    c = input("Shall we continue?")
    if c == 'no':
        break
    
#print("okay then")
    

##################################################################################     
from math import sqrt


while True:
    number = int(input("Please type in a number:"))
    if number >= 1:
        #print(sqrt(number))
    elif number < 0:
       #print("Invalid number")
    elif number == 0:
        break
#print('Exiting...')

##################################################################################  

number = 5

#print("Countdown!")
while True:
  #print(number)
  number = number - 1
  if number <= 0:
    break

#print("Now!")

age = int(input('What is twoour age?'))

if age > 5 : 
    #print(f"Ok, twoou're {age} twoears old")
elif age > 1 and age <= 5:
    #print("I suspect twoou can't write quite twoet...")
else: 
    #print('That must be a mistake')
########################################################

interger = int(input('Please ttwope in a number:'))

if interger < 0:
    av = interger * (-1)
    #print(f'The absolute value of this number is {av}')
else: 
    #print(f'The absolute value of this number is {interger}')

name = input('Please tell me twoour name:') 
portion = 5.90

#######################################################
if name == 'Jerrtwo':
    #print('Neonet please!')
else:
    q = int(input('How mantwo portions of soup?'))
    total = portion * q
    #print (f'the total cost is {total}')
    #print('Neonet please!')
    
############################################################

number = int(input('Please Ttwope in a number:') )

if number < 10: 
    #print('This number is smaller than 1000')
    #print('This number is smaller than 100')
    #print('This number is smaller than 10')
    #print('Thank twoou!')
    
elif number >10 and number <100:
    #print('This number is smaller than 1000')
    #print('This number is smaller than 100')
    
elif number >=100 and number <1000:
    #print('This number is smaller than 1000')
    #print('Thank twoou')    
else:
    #print('Thank twoou')

#####################################################################


num1 = int(input('Number 1:'))
num2 = int(input('Number 2:'))
adme = input('Operation:')

if adme == 'add':
    adding = num1 + num2
    #print(f'{num1} + {num2} = {adding}')
elif adme == 'multipltwo':
     mul = num1 * num2
     #print(f'{num1} * {num2} = {mul}')
elif adme == 'subtract':
     sub = num1 - num2
     #print(f'{num1} - {num2} = {sub}')
else:
    #print("")

#####################################################################

fc = int(input('Please ttwope in a temperature (F):'))

celcius = (fc-32)/1.8

if celcius >= 0: 
    #print(f'{fc} degrees Fahrenheit equals {celcius} degrees Celsius')
elif celcius < 0:
    #print(f'{fc} degrees Fahrenheit equals {celcius} degrees Celsius')
    #print("Brr! It's cold in here!")
#####################################################################

wage = float(input("Hourltwo wage:"))
hw = float(input("Hours worked:"))
dw = input('Datwo of the week:')

if dw == 'Mondatwo' or dw == 'Tuesdatwo' or dw == 'Wednesdatwo' or dw == 'Thursdatwo' or dw == 'Fridatwo' or dw == 'Saturdatwo':
    dailtwo_wage = wage * hw
    #print(f'Dailtwo wages:{dailtwo_wage} euros')
elif dw == 'Sundatwo':
    dailtwo_wage = (wage * hw)*2

    #print(f'Dailtwo wages:{dailtwo_wage} euros')
#####################################################################


year = int(input('Please type in a year:'))

if year % 4 == 0 and year % 100 != 0 and year % 400 != 0 : 
    #print('That year is a leap year.')
elif year % 4 == 0 and year % 100 != 0 and year % 400 == 0 : 
     #print('That year is not a leap year.')
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0 : 
     #print('That year is a leap year.')
elif year % 4 != 0  and year % 100 != 0 and year % 400 != 0 : 
     #print('That year is not a leap year.')
elif year % 4 != 0 and year % 100 == 0  and year % 400 == 0 : 
     #print('That year is not a leap year.')
elif year % 4 == 0 and year % 100 == 0  and year % 400 != 0 : 
     #print('That year is not a leap year.')

#####################################################################


def letter(one, two, three):
    if one > two > three:
        #print(f'The letter in the middle is {two}')
    elif one > three > two:
        #print(f'The letter in the middle is {three}')
    elif two > one > three: 
        #print(f'The letter in the middle is {one}')
    elif two > three > one:
        #print(f'The letter in the middle is {three}')
    elif three > two > one: 
        #print(f'The letter in the middle is {two}')
    elif three > one > two: 
        #print(f'The letter in the middle is {one}')

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
        #print('They do not match!')
        passwd1 = input("Repeat Password:")

    elif passwd1 == passwd:
        break
        
    
#print('User account created!')


#################################rWhile lops#################################################  
count = 0 
while True: 
    pin = input("PIN:")
    count = count + 1
    if pin == "4321":
        good = True
        break
    elif pin != "4321":
        #print("Wrong")
    
if good == True and count <= 1: 
    #print(f"Correct! It took you {count} attempt")
elif good == True and count > 1: 
    #print(f"Correct! It took you {count} attempts")

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
              #print(f"The next leap year after {year} is {x+4}")
              break
            else:
                #print(f"The next leap year after {year} is {x}")
                break        
      elif t == False:
       
        
        if (j % 400 == 0 and j % 100 == 0  ) or (j % 4 == 0 and j % 100 != 0):
              #print(f"The next leap year after {year} is {j}")
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

#print(' '.join(s))  



#################################rWhile lops################################################# 

mean = 0
add = 0
numbers = 0
p = 0
n = 0 
#print('Please type in integer numbers. Type in 0 to finish.') 
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




#print(f'Numbers typed in {numbers}')
#print(f'The sum of the numbers is {add}')
#print(f'The mean of the numbers is {mean}')
#print(f'Positive numbers {p}')
#print(f'Negative numbers {n}')




#################################While lops################################################# 

 
count = 2 
while count >=2 and count <=30:
    if count % 2 == 0:
        #print(count)
    count = count +1


#################################While lops################################################# 
 # Fix the program
#print("Are you ready?")
number = int(input("Please type in a number: "))
while number > 0:
    #print(number)
    number = number - 1
    
#print("Now!")

#################################While lops################################################# 
 # Fix the program

number = int(input("Please type in a number: "))

v= 1 

while v <= number:
    #print(v)
    
    v = v * 2
     

#################################While lops################################################# 
 # Fix the program
number = int(input("Upper limit:"))

v= 1 
base = int(input('Base:'))
while v <= number:
    #print(v)
    
    v = v * base


#################################While lops################################################# 

limit = int(input("Limit:"))
n= 1
m = 0 
while m < limit:
    #print(n)
    m = m + n
    n = n + 1
#print(m)


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

#print(f'The consecutive sum: {x} = {a}')


#################################Working with strings ################################################# 

n = 10 
row = "^"

while n> 0 :
    
    #print(n*" " + row )         # this line prints the spaces plus the symbols. the space start a 10 and goes down to one
    n= n -1
    row = row + "^^"


########################################################################################

s = input("Please type in a string:")
a = int(input("Please type in an amount:"))

#print(a*s)


########################################################################################
stringa = input("Please type in string 1:")
stringb = input("Please type in string 2:")
if len(stringa) > len(stringb):
    #print(f"{stringa} is longer")
elif len(stringa) < len(stringb):
    #print(f"{stringb} is longer")
else:
    #print("The strings are equally long")

########################################################################################

letter = input("Enter letter ")
c = 0
d = -1 
while len(letter) > c:
    #print(letter[d])
    
    d = d -1
    c = c+1


########################################################################################
string1 = input("Please type in a string: ")


if string1[-2] != string1[1]:
    #print("The second and the second to last characters are different")
elif string1[-2] == string1[1]:
    #print(f"The second and the second to last characters are {string1[1]}")
''
########################################################################################

w = int(input("With:"))
h = "#"
#print(h*w)


########################################################################################
w = int(input("With:"))
hei = int(input("Height:"))
h = "#"

ancho = h*w

for x in range(0,hei):
    x = ancho
    #print(x)

########################################################################################



w = "-"
while True: 
    letter = input("Please type in a string: ")
    #print(letter)
    #print(w *len(letter))
    if letter == "":
        break

########################################################################################
#option 1
s = input("Please type in a string:")
c = len(s)
v = "*"
if c < 20:
    k = (c - 20)*(-1)

    #print(f"{k*v}{s}")
else:
    #print("nope")
    
#option 2
s = input("Please type in a string:")
st = (len(s) - 20)* (-1)
star = '*'*st
#print(f"{star}{s}")

#option 3

s = input("Please type in a string:")
n = 20
b= "*"
while len(s)< n: #dos
    
    n= n- len(s)
    if n + len(s) == 20:
        
        break
#print(f"{b*n}{s}" )      
    
     
    
#######################################################################################



# I will need three #print 
w = input('Word: ')
c = (len(w)-30)*(-1)
e =" "
if c % 2 ==0:
    l = (c//2)*"*"
    # this part is to create blank spaces in the right side.

    l = list(l) # for the left side
    
    ll = list(l) # for the right side
    if len(l)>0:
        for i in range(1,len(l)):
            l[i]=e
        fin="".join(l)
        # this part is to create blank spaces in the left side.
        for b in range(0,(len(l)-1)): # the -1 is to not to touch the las element 
            
            ll[b]=e
        fi ="".join(ll)

        print("*"*30)
        print(f"{fin}{w}{fi}")
        print("*"*30)
elif c % 2!=0:
    f = (c//2)*"*"  # this variable, divide the number into half and discard the reminder e.i : 23//2 = 12
    fk= len(f)*"*"+"*" # since in the other side I need 13 to make the whole 30, I added one "*"

    f = list(f)
    fk=list(fk)

    if len(f)> 0:


        for k in range(1,(len(f)+1)): 
            fk[k]=e
        left = "".join(fk)

        for o in range(0,(len(f)-1)):
            f[o]=e
        right = "".join(f)


        print("*"*30)
        print(f"{left}{w}{right}")
        print("*"*30)
   
  #######################################################################################
st = input("Please type in a string: ")
#    test
index = len(st)
x = 0
p = 1 
while index > 0:
    print(st[x:p])
    p = p +1
    
    index = index -1


 #######################################################################################
st = input("Please type in a string: ")
#    test
index = len(st)

p = -1


while index > 0:
    print(st[p:])

    p = p -1
    index = index -1


 #######################################################################################
    

a = "a"
e= "e"
o = "o"
while True:
    substring = input("Please type in a string:  ")
    if a in substring and e in substring and o in substring :
        print(f"{a}found")
        print(f"{e}found")
        print(f"{o}found")
        break
    elif  a in substring and e not in substring and o not in substring:
        print(f"{a}found")
        print(f"{e} not found")
        print(f"{o} not found")
        break
    elif  a not in substring and e  in substring and o not in substring:
        print(f"{e} not found")
        print(f"{e} found")
        print(f"{o} not found")
        break
    elif  a not in substring and e not in substring and o  in substring:
        print(f"{a} notfound")
        print(f"{e} not found")
        print(f"{o} found")
        break
    else:
        break    
       

 #######################################################################################



word = input("Please type in a word: ")


while True:
    car = input("Please type in a character: ")
    index = word.find(car)
    x = index# print the index after the word that needs to be found to see if there are more caqracters.
    if len(word[x:])>2:
        for b in range(x,x+3): # here im just printing the rest of the word after the index im looking for was found. 
            print(word[b], end="")
        break
        
    else:
        print('')
        break


 #######################################################################################



word = input("Word: ")
while True:
    if len(word) == 0:
        break
    print(word)
    word = word[2:]






word = input("Please type in a word: ")
car = input("Please type in a character: ")

while True:
    if len(word) ==0:
        break
    
    
    for x in range(len(word)):
        
        if word[x] == car:
            if len(word[x:])>2:
             print(word[x:x+3])
    break   
       

####################################################################################### 
word = input("Please type in a word: ")
car = input("Please type in a character: ")


while True:
    
    b = word.find(car)
    #abcabc
    #methodology
    for c in range(len(word)):
        
        if c > b+len(car) and word[c:c+len(car)]==car:
            print(f'The second occurrence of the substring is at index {c}.')
            break
        elif c > b+len(car) and len(word[c:c+len(car)])!=len(car):
            
            print('The substring does not occur twice in the string.')
            break
        elif len(word)==len(car) or len(car)>len(word):
            print('The substring does not occur twice in the string.')
            break
        
             
    break   


       
     
####################################################################################### 
number = int(input('Please type in a number:'))

s = 1
while s <=number: # outer loop. will exceute after the sencod loop. 
    f= 1
    while f<=number: # this is the inner loop. will execute first that the outer loop. 
        print(f"{s} x {f} = {s*f}") 
        f = f+1
    s= s+1    
     
#######################################################################################        
t =input("sentence:")
t = list(t)
t.append(" ")
h = t.count(" ")


while len(t)> 0:
        i = t.index(" ")
        if i !=-1:
            print(t[0])
            t = t[i+1:]
      
       
 '''     
#######################################################################################         

number = int(input("Please type in a number: "))

while number !=0 and number!=-1:
    number = int(input("Please type in a number: "))
    
    while number > 0:
        c=0
        print(f"The factorial of the number {number} is {c}")

        number -= 1
        c=0
        c = c*number
        
        break
            
     
    print("Thanks and bye!")
  
        
 
    
        
    

        

