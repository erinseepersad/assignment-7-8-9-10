"""
Erin Seepersad 4/17/23	CSCI-UA 2 - 006
Assignment #9 Problem #1
"""

#PART A
def valid_username(xusername):
    #username=input("enter a username: ")
    #is the username valid
    if len(xusername)<5:
        return False
    elif xusername[0].isdigit():
        return False
    #elif username in range(97,122) or range(48,57) or range(48,57):
    elif xusername.isalnum():
         return True
    return False
print( valid_username('abc123') )    # True
print( valid_username('abcde')  )    # True
print( valid_username('abc')    )    # False
print( valid_username('@#$%^')  )    # False 
print( valid_username('1abcde') )    # False 
print( valid_username('')       )    # False 

#PART B

def username_exists(xusername):
    file_object = open('user_info.txt', 'r')
    content= file_object.read()
    splitdata=content.split('\n')
    #print(splitdata)
    addingusername=[]
    for i in splitdata:
        spliti=i.split(',')
        addingusername.append(spliti[0])
    if xusername=='':
        return False
    if xusername in addingusername:
        return True
    else:
        return False 
    file_object.close()
# split by line then split by comma then add the usernames in the list 
    
    if xusername=='':
        return False
    if xusername in content:
        return True
    else:
        return False
     
print( username_exists('pikachu')           )   # True
print( username_exists('charmander')        )   # True
print( username_exists('squirtle')          )   # True
print( username_exists('Pidgey2020')        )   # True
print( username_exists('SquirtleSquad99')   )   # False
print( username_exists('eevee')             )   # False
print( username_exists('bobcat')            )   # False
print( username_exists('')                  )   # False


#PART  B - username and password 
def check_password(xusername, xpassword):
    file_object = open('user_info.txt', 'r')
    content= file_object.read()
    splitdata=content.split('\n')
    addingusername=[]
    addingpassword=[]
    for i in splitdata:
        if len(i)>1:
            spliti=i.split(',')
            print(spliti)
            addingusername.append(spliti[0])
            addingpassword.append(spliti[1])
#find the index for username and then go to the corresponding list and compare with argument 
    if xusername in addingusername:
        index=addingusername.index(xusername)
        correspondinganswer=addingpassword[index]
        if correspondinganswer==xpassword:
            return True
    #if xusername in addingusername and xpassword in addingpassword:
        #return True
    if xusername=='' and xpassword=='':
        return False
    else:
        return False
    file_object.close()
print( check_password('pikachu', 'Abc123')              )    # True
print( check_password('squirtle', 'SquirtleSquad99')    )    # True
print( check_password('fearow', 'Pqr123')               )    # False
print( check_password('foobar', 'Hello123')             )    # False
print( check_password('', '')                           )    # False

#PART D
import datetime
def send_message(sender, recipient,message):
    filename='messages/'+recipient+'.txt'
    file = open(filename, 'a')
    d = datetime.datetime.now()
    month = d.month
    day = d.day
    year = d.year
    hour= d. hour
    minute= d.minute
    second= d.second
    message_str= sender +'|'+ str(month)+'/'+str(day)+'/'+str(year)+ ' '+ str(hour)+':'+str(minute)+':'+str(second)+'|'+ message+'\n'
    file.write(message_str)
    file.close()
send_message('pikachu', 'charmander', 'Hey there!')
send_message('charmander', 'pikachu', 'Good to see you!')
send_message('pikachu', 'charmander', 'You too, ttyl')

#PART C
def add_user(x,y):
    if username_exists(x)== False:
        file_object = open('user_info.txt', 'a')
        file_object.write('\n'+x+','+y)
        file_object.close()
        send_message('admin',x,'Welcome to your account!')# i dont think this is working 
        return True
    elif valid_username(x)== False:
        return False
add_user('foobar', 'abcABC123')
add_user('barfoo', 'xyz123ABC')
add_user('foobar', 'aTest123') # this should fail



#PART E
def print_messages(username):
    path = 'messages/'+username+'.txt'
    file= open(path, 'r')
    messages=file.read()

    messagecounter = 0
    messages_split = messages.strip().split('\n')
   
    for message in messages_split:
        messagecounter+=1
    
        line_split = message.split('|')#making a list of those three things
      
        print('Message',messagecounter,'received from',line_split[0])
        print('Time',line_split[1])
        print(line_split[2])
        
print_messages('charmander')            

#PART 2E
def delete_messages(username):
    path= 'messages/'+username+'.txt'
    file= open(path,'w')
    file.write('')
    file.close()
delete_messages('username')

#PART F
while True:
    pickachoice=input('(l)ogin,(r)egister or (q)uit: ')
    pickachoice=pickachoice.lower()
    if pickachoice=='r':
        print('Register for an account')
        username=input("Username(case sensitive): ")
        password= input('Password(case sensitive): ')
        add_user(username,password)
    elif pickachoice=='l':
        print('Log in')
        username=input("Username(case sensitive): ")
        password= input('Password(case sensitive): ')
        if username != valid_username(username) and password!= check_password(username,password):
            print('you have been logged in successfuly as',username)
            choice=input('(r)ead messages, (s)end message,(d)elete messages or (l)ogout: ')
            choice=choice.lower()
            if choice=='l':
                print('logging out as',username)
            elif choice=='r':
                add_user(username,password)
                print_messages(username)
                if print_messages=='':
                    print('No messages in your inbox')
            elif choice=='d':
                delete_messages()
                print('all messages deleted')
            elif choice=='s':
                print('type your message: ')

                
        else:
            print('invalid')
                
    if pickachoice=='q':
        print('goodbye!')
        break
    else:
        print('invalid, registration cancelled')
