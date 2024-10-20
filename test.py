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
        
              

