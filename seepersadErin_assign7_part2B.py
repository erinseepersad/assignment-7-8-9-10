"""
Erin Seepersad	4/06/23	CSCI-UA 2 - 006
Assignment #1 Problem #2B
"""
import seepersadErin_assign7_part2A
while True:
    encoding= input("Enter an encoding pattern,'end' to end: ")
    if encoding== 'end':
        break
    encodedecode= input("Enter a word to encode/decode: ")
    word = encodedecode
    for x in encoding:
    #for a in encoding== 'a':
        if x=='A':#add one 
            word= seepersadErin_assign7_part2A.add_letters(word,1)
            print('* Added 1 charatcer: ', word)
        elif x=='X':#delete one
            word= seepersadErin_assign7_part2A.delete_characters(word,1)
            print("* Deleted 1 character: ", word)
        elif x=="F":#flippp
            word= seepersadErin_assign7_part2A.flip(word)
            print("* Flipped: ",word)
        elif x=='U':#shift up
            word= seepersadErin_assign7_part2A.ascii_shift(word,1)
            print("* ASCII Shifted up: ", word)
        elif x=='D':#shift down
            word= seepersadErin_assign7_part2A.ascii_shift(word,-1)
            print("* ASCII Shifted down: ", word)
        elif x== 'L':#left
            word= seepersadErin_assign7_part2A.shift_left(word)
            print('* Shifted left: ', word)
        elif x=='R':#right
            word=seepersadErin_assign7_part2A.shift_right(word)
            print('* Shifted Right: ', word)
        else: 
            continue
    print()
    #notes from tutor:
  #going based on add character which has random therefore it is sloghtly differnt       
    #print
    #print("* Flipped: ",seepersadErin_assign7_part2A.flip(encodedecode))
    #print('* ASCII shfited down:',
    #print('* ASCII shifted up: ',
        #print("* Deleted 1 character: '",seepersadErin_assign7_part2A.delete_characters(encodedecode)) 
# everything is running except for the first example
#tutor said: my code is right and the first one will never match up because of the random function since added characters is first! whew!!!
