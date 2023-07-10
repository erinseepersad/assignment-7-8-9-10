"""
Erin Seepersad	3/30/23	CSCI-UA 2 - 006
Assignment #7 Problem #1
I helped Beverly Ajao
"""
# function:   string_length
# input:      a word (String)
# processing: computes the length of the supplied String (without using the len() function)
# output:     returns the length of the string (integer)
def string_length(x):
    counter=0
    for i in x:
        counter+=1
    return counter

# sample code:
print ( string_length("apple") )	# 5
print ( string_length("pear")  )	# 4
print ( string_length("")      )	# 0

# function:   string_isalpha
# input:      a word (String)
# processing: determines if the supplied String contains all alphabetic characters (A-Z,a-z)
#             DO NOT USE THE "isalpha()" METHOD or any other String methods! You may
#             use the 'ord' and 'chr' functions though.
# output:     returns True of False (boolean)
def string_isalpha(x):
    boo=True
    if x==(""):#do if statement for an empty string
        boo=False
    else:
        for i in x:
            table=ord(i)
            if table >= 65 and table<=90:
                boo=True
            elif table >= 97 and table <=122:
                boo=True
            else:# if there one character that is not an alpha bedded character then you can directly return false( number or special character)
                return False
    return boo
"""
def string_isalpha(x):#didnt run
    loweralpha= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upperalpa= ['A','B','C','D','E','F','G','H','I','J','K','L','N','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    if x (loweralpha['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26']):
        return True
    if x(upperalpa['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26']):
        return True
    else:
        return False

def string_isalpha(x):#ran but all true 
    loweralpha= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upperalpa= ['A','B','C','D','E','F','G','H','I','J','K','L','N','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for x in loweralpha:
        return True
    for x in upperalpa:
        return True
    if x!=loweralpha and x!=upperalpa:
        return False
  """    
# sample code:
print ( string_isalpha("apple")     )	# True
print ( string_isalpha("pear!")     )	# False
print ( string_isalpha("123")       )	# False
print ( string_isalpha("123 AbC")   )	# False
print ( string_isalpha("abc1")      )	# False
print ( string_isalpha("")          )	# False

# function:   string_adjustcase
# input:      a word (String) and a case type (String)
# processing: consults the case type (either "upper" or "lower") and converts all alphabetic 
#             characters in the word to their desired equivalents.  will return the original 
#             phrase if the case type is invalid.
#             DO NOT USE THE "lower()" METHOD OR "str.lower()"! or any 
#             other String methods! you may use the 'ord' and 'chr' functions though, if you wish.
# output:     returns a new copy of the String
def string_adjustcase(x,y):
    if y== 'upper' or y=='lower':
        newstring=''
        for i in x:
            table=ord(i)
            if table >= 65 and table<=90: #upper
                if y=='lower':# go to lowercase
                    newstring+= chr(table+32)
                else:
                    newstring+= chr(table)
            elif table >= 97 and table <=122:#lower
                if y=='upper':#go to uppercase
                    newstring+=chr(table-32)
                else:
                    newstring+= chr(table)
            else:
                newstring+=chr(table)
        return newstring
    else:
        return x
     
        
# sample code:
print ( string_adjustcase("apple", "upper")     )		# APPLE
print ( string_adjustcase("APPLE", "lower")     )		# apple
print ( string_adjustcase("aPPlE", "lower")     )		# apple
print ( string_adjustcase("APPLE", "pikachu")     ) 		# APPLE
print ( string_adjustcase("Hello World!", "lower")     )	# hello world!
print ( string_adjustcase("", "lower")     )			# nothing prints

# function:   string_capitalize
# input:      a phrase (String)
# processing: capitalizes the first alphabetic character of each word in a string, 
#             and lowercases all other alphabetic characters.  For example:
#
#             "hello world" -> "Hello World"
#             "HELLO WORLD" -> "Hello World"
#
#             DO NOT USE THE "capitalize()" or "title()" METHODS, 
#             or any other String methods!
#             You can use 'ord', 'chr' or any other functions that you wrote for this
#             part of the assignment.
#
#             Hint: you might need to iterate over the supplied phrase and test to see
#             if a character is preceded by a space in order to solve this question.
# output:     returns a new copy of the String
def string_capitalize(x):
    newstring = ""
    previous_character = " "
    for i in x:
        table=ord(i)
        if previous_character == " ":
            if table>96:
                newstring += chr(table - 32)
            else:
                newstring+=i
        else:
            if table>=65 and table<=90:#range for all the capital letters
                newstring+= chr(table+32)
            else:# everything that doesnt fall into this we dont change 
                newstring+=i
        previous_character = i
    return newstring
    
# sample code:
print( string_capitalize("happy birthday sad kitten") )
# Happy Birthday Sad Kitten

print( string_capitalize("every word in this phrase should start with a capital letter") )
# Every Word In This Phrase Should Start With A Capital Letter

print( string_capitalize("EVERYTHING IS UPPERCASE ALREADY!") )
# Everything Is Uppercase Already!

print( string_capitalize("cRaZy MIxeD cAse") )
# Crazy Mixed Case

