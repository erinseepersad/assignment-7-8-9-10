"""
Erin Seepersad	4/13/23	CSCI-UA 2 - 006
Assignment #8 Problem #2

"""
import wordle
import random

allwords = wordle.words
tries=0
wins=0
gameslost=0
def wordlegame(tries,wins,gameslost):
    #print( len(allwords), "words available." )remove for part 2b
    thewordle=random.randint(0,len(allwords)-1)
    #print('The Wordle is',
    allwords[thewordle].upper()
    #print()
    print('          WORDLE')
    print('------------------------------')
    checking2 = ''
    x=''
    counter= 0#tries per game 
    highestscore=6
    totalscore=0
    totalgames=0
    averagescore=0
    while True:
        #for i in range(6):
        counter+=1
        guessing=input('guess the word: ').lower()
        #print(counter,tries,wins)
        #print(guessing)
        if guessing.lower()==allwords[thewordle]:
            print('Correct! The wordle is',allwords[thewordle].upper())
            print('You guessed the Wordle in',counter,'tries')
            tries+=counter
            wins+=1
            playagain=input('Do you want to play again? (Y) or (N) ').upper()
            if playagain.upper()=='Y':
                highestscore=min(highestscore,counter)
                wordlegame(tries,wins,gameslost)
                break
            elif playagain.upper()=='N':
                totalscore+=counter
                highestscore=min(highestscore,counter)
                totalgames+=1
                if wins==0:
                    print('Average Score:', 0)
                else:
                    averagescore=tries/wins
                    print('Average Score: ',averagescore)
                print('High Score: ',highestscore)
                print('Number of games lost:',gameslost)
                break
            else:
                print('Invalid Response')
                playagain=input('Do you want to play again? (Y) or (N) ').upper()
            break
        elif len(guessing)!=len(allwords[thewordle]):#length check
            print('You must enter a 5 letter word')
            guessing=input('guess the word: ').lower()
        elif guessing.lower() not in allwords: #number check
            #print(guessing)
            print('Invalid word')
            guessing=input('guess the word: ').lower()
        #check each letter in the words
        checking='' #add it to later 
        for i in range (len(allwords[thewordle])):
            if guessing[i]== allwords[thewordle][i]:
                checking+=guessing[i].upper()+'* '
            elif guessing[i] in (allwords[thewordle]):
                checking+= guessing[i].upper()+'? '
            else:
                checking+=guessing[i].upper()+'  '
        checking2 += checking + '\n'
        print(checking2)
        if counter==6:
            print('Sorry you did not guess the Wordle. The Wordle is',allwords[thewordle].upper())
            gameslost += 1
            playagain=input('Do you want to play again? (Y) or (N) ').upper()
            if playagain.upper()=='Y':
                wordlegame(tries,wins,gameslost)
                break
            elif playagain.upper()=='N':
                #gameslost += 1
                print('Number of games lost:',gameslost)
                print('High Score: ',highestscore)
                if wins==0:
                    print('Average Score:', 0)
                else:
                    averagescore=tries/wins
                    print('Average Score: ',averagescore)
                break
            else:
                print('Invalid Response')
                playagain=input('Do you want to play again? (Y) or (N) ').upper()      
          
    
        
        
wordlegame(tries,wins,gameslost)

#to do
#format- said it was correct
#how to print the sixthtime- checked
#check each letter in the words
"""
        checking='' #add it to later 
        for i in range (len(allwords[thewordle])):
            if guessing[i]== allwords[thewordle][i]:
                checking+=guessing[i].upper()+'* '
            elif guessing[i] in (allwords[thewordle]):
                checking+= guessing[i].upper()+'? '
            else:
                checking+=guessing[i].upper()+'  '
        checking2 += checking + '\n'
        print(checking2)
if guessing not in allwords: #number check
        print(guessing)
        print('Invalid word')
        guessing=input('guess the word: ').upper()
    else:
        break
 #guessing=input('guess the word: ').upper()
    #print(guessing)
    #print(allwords[1:15])
 #for i in range(len(scores)):
                    #totalscore+=scores[i]#add all of scores into this then calculate average below
#totalgames+=1
                #ighestscore=counter
                #averagescore= total/highestscore
#else:#when it is true break it-- all conditons met
            #break
#totalscore+=scores[i]#add all of scores into this then calculate average below
#total=counter
#highestscore=counter
    #scores.append(counter)
            #averagescore= total/highestscore
        # line 19 accumator checking,
        #for loop--> 37 is the blank checkign and then 38-44
        #u add things tho the blank checking based on the word you
        #entered previously then in 45 you add on whatevr you did in
        #checking to the accumlator
"""

