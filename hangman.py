#Hangman Game

#Repeat
repeatWhole=0
while repeatWhole==0:

#Rules
    print("Hello, this is a game of hangman.")
    print("You will lose if you make 10 wrong guesses.")
    print("You will be able to select your own word, or have a random word")

#Random word
    print("\nAnswer with 'yes' or 'no'")
    random=str(input("Would you like to enter your own word: "))
    if random=="yes" or random=="Yes":
        word=str(input("\nEnter your word here:"))
    else:

    #Add words to this word list
        wordList=["sunday","kit","abuse","coma","protection","slap","see","courage","fail","acceptable","stereotype","bomber","waste","extension","adoption","inhabitant","groan","liability","wait","remark","strange","board","ramen",
                  "bend","elegant","culture","ruin","devote","deficit","incredible","classify","decrease","generate","presidential","labour","cream","trace","exploration","education","week","whip","communication","rational","heroin",
                  "admiration","dance","facility","persist","discipline","ramen","love"]
        import random
        word=(random.choice(wordList))

#Underscores
    letterIndex=0
    underscore=""
    length=len(word)
    while letterIndex<length:
        underscore=underscore+"-"
        letterIndex=letterIndex+1
    underscore=list(underscore)
    output="".join(underscore)
    print("")
    print(output)
    substring="-"

#Guess the letters'
    word=word.lower()
    incorrectLetters=[]
    guesses=10
    end=0
    while guesses>0 and end==0:
        letterCount=0
        wrongGuess=0
        index=0
        individual=(word[index])
        guess=str(input("\nEnter your guess: "))
        guess=guess.lower()
        while index<length:
            individual=(word[index])
            if guess==individual:
                underscore[index]=guess
                output="".join(underscore)
                wrongGuess=1
                letterCount=letterCount+1
            index=index+1
        if wrongGuess==0:
            print("\nThere are no",guess+"'s")
            incorrectLetters.append(guess)
            guesses=guesses-1
            print("You have",guesses,"guesses left.")
            print("\nIncorrect letters:",incorrectLetters)
            print("")
            print(output)
        if wrongGuess==1:
            if letterCount>1:
                print("\nThere are",letterCount,guess+"'s")
            if letterCount==1:
                print("\nThere is 1",guess)
            print("")
            print(output)
        finishIndex=0
        questionContinue=0
        while finishIndex<length:
            if underscore[finishIndex]=="-":
                questionContinue=questionContinue+1
            finishIndex=finishIndex+1
        if questionContinue==0:
            end=1
        if guesses==0:
            end=2

#Final results
    if end==2:
        print("\nYou lose")
        print("The correct answer was:",word)
    if end==1:
        finalGuesses=10-guesses
        print("\nCongradulations!!")
        print("You made",finalGuesses,"wrong guesses.")
            
#Repeat?
    invalidRepeat=0
    while invalidRepeat==0:
        print("\nAnswer with 'yes' or 'no'.")
        repeatAnswer=str(input("Would you like to play again: "))
        if repeatAnswer=="yes" or repeatAnswer=="Yes":
            print("")
            invalidRepeat=1
            repeatWhole=0
        elif repeatAnswer=="no" or repeatAnswer=="No":
            invalidRepeat=1
            repeatWhole=1
            print("\nOk, have a good day!")
        else:
            print("\nInvalid response!")
            print("Please try again.")
            repeatWhole=1
