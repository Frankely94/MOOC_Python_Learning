
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
'''


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
    x = (142000+(value-1000000)*0.17)
    print(f"Amount of tax: {x} euros")   