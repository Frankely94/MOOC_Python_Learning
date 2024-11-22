word = input("Please type in a word: ")
car = input("Please type in a character: ")


while True:
    
    v = word.find(car)

    for x in range(len(word)):
        if  word[x]==car and x > v+1:
            print(f"The second occurrence of the substring is at index {x}")
            break
        
    print("The substring does not occur twice in the string.")
          