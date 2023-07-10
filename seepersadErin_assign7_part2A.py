"""
Erin Seepersad	3/30/23	CSCI-UA 2 - 006
Assignment #7 Problem #2
I worked with Beverly Ajao for function 5
Tutor said I can comment the Sample Programs in reagrds to importing for 2B!
"""
#Function 1
# function:   ascii_shift
# input:      a word to shift (String) and an amount to shift by (integer) string is in x amount is in y
# processing: shifts each character in the supplied word to another position in the ASCII
#             table. the new position is dictated by the supplied integer.  for example,
#             if word = "apple" and num=1 the newly generated word would be:
#
#             bqqmf
#
#             because we added +1 to each character. if we were to call the function with
#             word = "bqqmf" and num=-1 the newly generated word would be:
#           
#             apple
#
#             because we added -1 to each character, which shifted each character down by
#             one position on the ASCII table.
#
1#             in the event that an empty string is supplied no shift will occur and an empty 
#             string should be returned
#
# output:     returns the newly generated word
def ascii_shift(x,y):
   #newword=chr(ord+x)
    word2=''
    for newword in x:
        word2+= chr(ord(newword)+y) #how much we shift depends on argument y
    return word2
"""
#Funtion 1 Program      
word = "ABCDEFG"
for i in range(-5, 6):
    print ("ASCII shifting", word, "by", i, "=>", ascii_shift(word, i))
"""    
#Function 2
# function:   shift_right
# input:      a word to shift (String)
# processing: shifts all characters in the string to the right. the last character in the string
#             will be shifted to the beginning of the string.  for example:
#
#             apple -> eappl
#
#             in the event that an empty string is supplied no shift will occur and an empty 
#             string should be returned
#
# output:     returns the newly generated word  
def shift_right(x):
    #word2=''
    #newstring=''
    #if word2=='':
        #newstring += chr(ord(word2) + 1)#logic error-- prints words, just not the correct ones
    x= x[-1]+ x[0:-1]
    return x
"""
#Function 2 Program 
word = "hello world!"
print("Shifting right", word, "=>", shift_right(word))
"""
#Function 3
# function:   shift_left
# input:      a word to shift (String)
# processing: shifts all characters in the string to the left. the first character in the string
#             will be shifted to the end of the string.  for example:
#
#             apple -> pplea
#
#             in the event that an empty string is supplied no shift will occur and an empty 
#             string should be returned
#
# output:     returns the newly generated word
def shift_left(x):
    x= x[1:]+x[0]
    return x
"""
#Function 3 Program
word = "hello world!"
print("Shifting left", word, "=>", shift_left(word))
"""
#Function 4
# function:   flip
# input:      a word to flip (String)
# processing: flips the first half of the string with the second half of the string.
#             if the string has an even number of characters this function will work as follows:
#
#             ABCD -> CDAB
#
#             if the string has an odd number of characters this function will work as follows:
#
#             ABCDE -> DECAB
#
#             in the event that an empty string is supplied no flip will occur and an empty 
#             string should be returned
#
# output:     returns the newly generated word
def flip(x):
    n=len(x)
    if n%2==0:# even
        x= x[-(n//2):]+x[:(n//2)]
    else:#odd
        x= x[(n//2)+1:]+x[(n//2)]+x[:(n//2)]
    return x
"""
#Function 4 Program
word = "ABCDEFG"
print ("Flipping", word, "=>", flip(word))

word = "123456"
print ("Flipping", word, "=>", flip(word))
"""

#Function 5 
# function:   add_letters
# input:      a word to scramble (String) and a number of letters (integer)
# processing: adds a number of random letters (A-Z; a-z) after each letter 
#             in the supplied word. for example, if word="cat" and num=1 
#             we could generate any of the following:
#             cZaQtR
#             cwaRts
#             cEaett
# 
#             if word="cat" and num=2 we could generate any of the following:
#             cRtaHFtui
#             cnnaNYtjn
#             czAaAitym
#
# output:     returns the newly generated word
def add_letters(word, num):
    import random
    counter= num
    newWord=''
    for i in word:
        numbers= random.randint(1,2)
        #for i in range(num)
        if numbers==1:
            newWord+=i
            for c in range(num):
                #word+ random.str(a,z)
                newWord+=chr(random.randint(97,122))
                #1. find the asccii for lower and upper case put that in for random th
	#then convert to character 
	#counter+=num 
        else:
            newWord+=i
            for c in range(num):
                newWord+= chr(random.randint(65,90))
    return newWord
                
        
    
"""	
#Function 5
	# define original word
original = "Hello!"

# loop to demonstrate the function
for num in range(1, 5):

    # scramble the word using 'num' extra characters
    scrambled = add_letters(original, num)

    # output
    print ("Adding", num, "random characters to", original, "->", scrambled)
    """
#Function 6
# function:   delete_characters
# input:      a word to analyze (String) and the number of characters to remove (integer)
# processing: the function starts at the first position in the supplied word and keeps it.
#             it then removes "num" characters from the word. the process is repeated again
#             if the word contains additional characters - the next character is kept
#             and "num" more characters are removed.  For example, if word="cZaYtU" and
#             num=1 the function will generate the following:
#        
#             cat (keeping character 0, removing character 1, keeping character 2, removing
#                  character 3, keeping character 4, removing character 5)
#
# output:     returns the newly unscrambed word
def delete_characters(word, num):
    new_word = ""
    newString=len(word)
    for i in range(newString):
        if i % (num+1) == 0:
            new_word += word[i]
    return new_word
"""
#Function 6 Program
word1 = "HdeulHlHom!t"
word2 = "HTLedklFNljioMH!bi"
word3 = "HHHZeZrflqSflzOiosNU!jBk"
word4 = "HFtRKeivFllRNlUlGTaooYwoH!JpXL"

unscrambled1 = delete_characters(word1, 1)
print ("Removing 1 characer from", word1, "->", unscrambled1)

unscrambled2 = delete_characters(word2, 2)
print ("Removing 2 characers from", word2, "->", unscrambled2)

unscrambled3 = delete_characters(word3, 3)
print ("Removing 3 characers from", word3, "->", unscrambled3)

unscrambled4 = delete_characters(word4, 4)
print ("Removing 4 characers from", word4, "->", unscrambled4)
"""

