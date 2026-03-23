#Number Guessing Game
while True:     #it is the Loop to allow playing again
    number=50   #we can change this number (secret number)
    attempts=7  #number of the attempts we can use is 7
    used_attempts=0  #initially it will be 0
    print("\nGuess the number between 1 and 100")
    print("You have 7 attempts!")
    while attempts>0: #if attempt is greater than 0 
        guess=int(input("Enter your guess: "))
        used_attempts+=1 #if we used attempts increases to 1
        attempts-=1     #the number of attempts gets reduces when we guess the number
        if guess==number:  #if guess num is equal to number then its guessed num is correct one and then break the loop 
            print(f"Congratulations! You guessed it in{used_attempts}attempts.")
            break
        elif guess<number:    #if guess num is less than actual num we have to conditions 
            print(f"Too low Attempts remaining:{attempts}")  #if it is less than then actual num shows too slow
        else:
            print(f"Too high Attempts remaining:{attempts}")  #if it more than the actual number than its shows the too high
    if guess!=number:
        print(f"You faileD The number was {number}")   # if the guess num is not equal than it will be failed 
    play_again=input("Do you want to play again (yes/no): ") #option for playing again
    if play_again.lower()!="yes":     #if user says anything than yes exit the game
        print("Thanks for playing!")
        break