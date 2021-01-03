def game():
    #setup
    game = True      
    wordlist =[]    
    currentgame=[]
    guesses = []

    #start
    print("How many lives do you have?")
    lives = input()
    print("input word")
    word = input()
    lives = int(lives)
    
    #layout blank space
    blanks = 0
    while blanks < 15:
        print("\n")
        blanks +=1

    #making the gameboard
    for i in word:
        currentgame.append("_")
        wordlist.append(i) 
    
    #Gamelayout
    print("=====Game=====") 
    print("\n")    
    print(*currentgame, sep=" ")
    print("\n")
    print("==============")
    print("=====Lives=====")
    print("Lives: "+str(lives))
    print("=====Guesses=====")
    print(*guesses, sep=" ")

    #Guessing
    while game == True:        
       
        guess = input()       
        
        if(len(guess)==1):
            guesses.append(guess)            
        else:
            print("Invalid guess. Only 1 letter at a time")

    
        #check if guess correct and fill in the right spot
        if guess in wordlist:
            for i in range(len(wordlist)):
                x = wordlist[i]
                if(x==guess):
                    currentgame[i] = x
            
            #Layout blankspace
            blanks = 0
            while blanks < 15:
                print("\n")
                blanks +=1
            
            #gamelayout
            print("=====Game=====") 
            print("\n")    
            print(*currentgame, sep=" ")
            print("\n")
            print("==============")
            print("=====Lives=====")
            print("Lives: "+str(lives))
            print("=====Guesses=====")
            print(*guesses, sep=" ")
        
        #remove lives    
        else:
            blanks = 0
            while blanks < 15:
                print("\n")
                blanks +=1           
            lives = lives-1

            #game layout
            print("=====Game=====") 
            print("\n")    
            print(*currentgame, sep=" ")
            print("\n")
            print("==============")
            print("=====Lives=====")
            print("Lives: "+str(lives))
            print("=====Guesses=====")
            print(*guesses, sep=" ")
            

        #Check if won
        if("_" not in currentgame):
            print("\n==========\n")
            print("You've won")
            print("\n==========\n")
            game = False

        #Check if lost
        if(lives==0 and "_" in currentgame):
            print("\n==========\n")
            print("You've lost")
            print("\n==========\n")
            print("The word was " +word)
            game = False
game()    

input()

        