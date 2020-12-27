#the required modules
import random
print(" Welcome to Password Generator :)")
f = open("PASS_LIST.txt","a+") # this opens a text file where the passwords will be stored for your use
#the actual program:

#the user interface

def storing_func(string):
    store = int(input("\n do you want to store the password in the text file? Type in 1 and 2 if no :"))
    if store == 1:
        reason = input(" Where will the password be used? :")   
        f.write("\n%s : %s" %(reason, string))
        print("\n THERE WILL BE A TEXT FILE NAMED PASS_LIST.txt IN THE FOLDER WHERE YOU'VE RUN THIS PROGRAM...")
        print("\n YOU CAN ALSO COPY THE PASSWORD FROM THERE :)")
        print("\n Thanks for using T's app")  
    if store == 2:
        print("\n Thanks for using T's app")    
#characters only: 
def char_only(pass_length):
    passwordlength=pass_length+1
    string = ""
    for j in range(0,passwordlength):
        k = random.randint(1,3)
        char = random.randint(65,90)
        if k == 1:
            string += str(chr(char)).lower()
        elif k == 2:
            string += str(chr(char)).upper()
    print("\n Here's your password: ",string)
    storing_func(string)


#characters and numbers:
def char_and_num(pass_length):
    passwordlength=pass_length+1
    string = ""
    for j in range(0,passwordlength):
        k = random.randint(1,4)
        char = random.randint(65,90)
        num = random.randint(0,10)
        if k == 1:
            string += str(chr(char)).lower()
        elif k == 2:
            string += str(chr(char)).upper()
        elif k == 3:
            string += str(num)
    print("\n Here's your password: ",string)
    storing_func(string)

#chars, numbers and special characters
def char_num_sp(pass_length):
    passwordlength=pass_length+1
    string = ""
    for j in range(0,passwordlength):
        k = random.randint(1,5)
        char = random.randint(65,90)
        num = random.randint(0,10)
        symbols = ['@', '#', '$', '%', '=', '?', '/', '|', '~', '>',  
           '*', '(', ')'] 
        if k == 1:
            string += str(chr(char)).lower()
        elif k == 2:
            string += str(chr(char)).upper()
        elif k == 3:
            string += str(num)
        elif k == 4:
            string += str(random.choice(symbols))    
    print("\n Here's your password: ",string)
    storing_func(string)
def program():
    print("\n Here are the various types of passwords that you could produce using this program")
    i = int(input("\n 1)just characters(lower and upper case)\n 2)characters and numbers\n 3)characters and numbers and special characters\n\n ENTER THE OPTION:"))
    pass_length = int(input("\n enter the length of the password (an ideal password would be more than 10 digits :) ): "))
    if i == 1:
       char_only(pass_length)
    if i == 2:
       char_and_num(pass_length)
    if i == 3:
       char_num_sp(pass_length)   
    if i != 1 and i != 2 and i != 3:
       print("\n INVALID CHOICE... RERUN THE PROGRAM AND ENTER A VALUE IN THE RANGE OF 1 to 3")

    conclusion = "COPY THE PASSWORD AND PASTE IT WHEREVER YOU WANT :)"

    print("\n",conclusion) 

    re_run=int(input("\n \n Do you want to run the program? type in 1 if yes and 2 if no :"))
    if re_run==1:
        program()
    if re_run==2:
        print("\nthanks again for sticking out here!")           

program()

