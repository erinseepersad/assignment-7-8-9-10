"""
Erin Seepersad	4/27/23	CSCI-UA 2 - 006
Assignment #10 Problem #1
I worked with Beverly Ajao.

file=open('songs/asItWas.txt','r')
content=file.read()
letters={
    'A':0
    'B':0
    'C':0
    'D':0
    'E':0
    'F':0
    'G':0
    'H':0
    'I':0
    'J':0
    'K':0
    'L':0
    'M':0
    'N':0
    'O':0
    'P':0
    'Q':0
    'R':0
    'S':0
    'T':0
    'U':0
    'V':0
    'W':0
    'X':0
    'Y':0
    'Z':0}
total=0
for i in content:
    if i.isalpha():
        total+=1
        if i.upper() in letters:
            letters[x.upper()]+=1
file.close()
print('enter a filename: ', file)
print('analyzing song...')
print()
print('there are',total,'letters in this song!')
print()
print('the song contains')


"""
filename=input('enter a filename: ')
filepath='songs/'+filename+'.txt'
try: 
    file=open(filepath,'r')
    content=file.read()
    data = ""
    for line in content:
        data += line.strip().upper()
    letters = {}
    total = 0
    for letter in data:
        if letter.isalpha():
            total += 1
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1
    if 'Z' not in letters:
        letters['Z']=0
        total+=1
    file.close()
    print('analyzing song...')
    print()
    print("There are a total of " + format(total, ',d') + " letters in this song!\n")
    print("The song contains:")
    print("Letter : Frequency")
    for letter in sorted(letters):
        percentage= letters[letter]/total* 100
        percentageformatted= format(percentage, '.2f')
        endpercentage='%'
        endpercentformatted= format(endpercentage, '>2s')
        print("  " + letter + "    : " + percentageformatted +endpercentformatted)
except FileNotFoundError:
    print('File not found')
#if alphat not in data append it letter=0
            #elif letter not in data:
             #   letters[letter]=0
              #  total+=1
 #sortedkeys= sort(letter.keys())
    #python gives sorted. you left off with sorted
    #sortedkeys=sorted(letter.keys())
    #print(sortedkeys)
