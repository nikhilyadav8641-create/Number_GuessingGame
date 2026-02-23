import random
randomNumber=random.randint(1,100)
count=0
while True:
    number=int(input("Enter the number in between 1 to 100 : "))
    if(number<randomNumber):
        print("The Guess number is low")
    elif number>randomNumber:
        print("The Guess number is High")
    else:
        print("The Guess number is correct")
        break
    count+=1
print(f"The number of attempt you made while playing the game {count}" )

   
    
    

