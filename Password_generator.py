#the required modules
import random


#the user interface
print(" Welcome to Password Generator :)")
print("\n Here are the various types of passwords that you could produce using this program")
i = int(input("\n 1)just characters(lower and upper case)\n 2)characters and numbers\n 3)characters and numbers and special characters\n\n ENTER THE OPTION:"))
f = open("PASS_LIST.txt","a+") # this opens a text file where the passwords will be stored for your use
reason = input(" Where will the password be used? :") 
#the actual program:

#characters only: 
def char_only():
    string = ""
    rand_char = random.randint(10,30) #this variable randomly chooses the length of the password
    for j in range(0,rand_char):
        k = random.randint(1,3)
        char = random.randint(65,90)
        if k == 1:
            string += str(chr(char)).lower()
        elif k == 2:
            string += str(chr(char)).upper()
    print(" Here's your password: ",string)
    f.write("\n%s : %s" %(reason, string))

#characters and numbers:
def char_and_num():
    string = ""
    rand_char = random.randint(10,30)
    for j in range(0,rand_char):
        k = random.randint(1,4)
        char = random.randint(65,90)
        num = random.randint(0,10)
        if k == 1:
            string += str(chr(char)).lower()
        elif k == 2:
            string += str(chr(char)).upper()
        elif k == 3:
            string += str(num)
    print(" Here's your password: ",string)
    f.write("\n%s : %s" %(reason, string))  

#chars, numbers and special characters
def char_num_sp():
    string = ""
    rand_char = random.randint(10,30)
    for j in range(0,rand_char):
        k = random.randint(1,5)
        char = random.randint(65,90)
        num = random.randint(0,10)
        symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
           '*', '(', ')'] 
        if k == 1:
            string += str(chr(char)).lower()
        elif k == 2:
            string += str(chr(char)).upper()
        elif k == 3:
            string += str(num)
        elif k == 4:
            string += str(random.choice(symbols))    
    print(" Here's your password: ",string)
    f.write("\n%s : %s" %(reason, string))             

#the execution of choices!
if i == 1:
    char_only()
if i == 2:
    char_and_num()
if i == 3:
    char_num_sp()   
if i != 1 and i != 2 and i != 3:
    print("\n INVALID CHOICE... RERUN THE PROGRAM AND ENTER A VALUE IN THE RANGE OF 1 to 3")

conclusion = "COPY THE PASSWORD AND PASTE IT WHEREVER YOU WANT :)" 

print("\n",conclusion)        
print("\n THERE WILL BE A TEXT FILE NAMED PASS_LIST.txt IN THE FOLDER WHERE YOU'VE RUN THIS PROGRAM...")
print("\n YOU CAN ALSO COPY THE PASSWORD FROM THERE :)")