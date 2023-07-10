"""
Erin Seepersad	4/27/23	CSCI-UA 2 - 006
Assignment #10 Problem #2
I worked with Beverly Ajao
"""
#2A
# function:   cleanup_string
# input:      a string to clean up
# processing: (1) makes the entire string lowercase.
#             (2) retains only alphabetic, numeric and space characters
#                 [all punctuation and special characters removed]
# output:     returns the cleaned up string
def cleanup_string(data):
    empty=''
    for i in data:
        if i.isalpha() or i.isnumeric() or i.isspace():
            empty+=i.lower()
    return empty



# TEST CODE
test1 = cleanup_string("Hello World! This is a simple test of this function!")
print (test1)
# hello world this is a simple test of this function

test2 = cleanup_string("ABC123abc this is Another TEST!!!#@@")
print (test2)
# abc123abc this is another test

test3 = cleanup_string("I'm so happy today! La la la la it doesn't get any better than this.")
print (test3)
# im so happy today la la la la it doesnt get any better than this

#2B
import os
files = os.listdir("data")
#print (files)

#lookingup={}#search
search={}
#2C
#bev help with setup:
#1. print all the words
#2. print letters, spaces, numbers
#3. individual 
for i in files:
    file=open('data/'+i,'r')
    content= file.read()
    file.close()
    newercontent=(cleanup_string(content))
    anothercontent=newercontent.split()
    for y in anothercontent:
        if y in search:
            if i not in search[y]:
                search[y]+=[i]
        else:
            search[y]=[i]
                
print ('happy:', search['happy'])
print ('cat:', search['cat'])
print ('rainbow:', search['rainbow'])
#print ('apple:', search['apple'])

# OUTPUT
'''
happy: ['aUAFHAlczU.txt', 'R2ECugDCAv.txt']
cat: ['jJG5h8GyyY.txt']
rainbow: ['L9fMTLX60i.txt', 'S0zDFkXpZW.txt']
RUNTIME ERROR (apple does not exist as a KEY in the dictionary)
'''
#2D
#bev:
#1. search for single word 2. word is equal to input 3. key in dictonary conintue
# do if not statements, concatenate same for display 
while True:
    options=input('search for a (s)ingle word or (q)uit: ')
    if options.lower()=="s":
        word=input('enter a word to search for: ')
        if word in search:
            length=(len (search [word]))
            print("'"+word+"'",'can be found in', length,'files')
            print ("These files are:")
            for z in range(len (search [word])): 
                print ("*", search [word][z])

        else: 
            print ("'"+word+"'","cannot be found")
            print ()
            continue

        asktodisplay=input ('display these files? (y/n): ')
        print ()
        if asktodisplay.lower()=="y":
            for z in range(len(search [word])):
                print ('*' , search [word] [z])
                filename= ("data/"+search [word] [z])
                file=open (filename, "r")
                newercontent=file.read()
                file.close()
                print(newercontent)
                print ()

        else:

            continue

    elif options.lower()=='q':
        break
    else:

        print ('invalid command')

        print ()
