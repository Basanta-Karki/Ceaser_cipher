import os

SELECTED_SHIFT=None

def welcome():

    print("Welcome to the Caesar Cipher" '\n'
    "This program encrypts and decrypts text with the Caesar Cipher")

welcome()


def enter_message():

    while True:

        print("Would you like to encrypt (e) or decrypt (d):")

        user_mode= input("e or d:").lower()

        if user_mode=="e" or user_mode=="d":
            break

        else:
            print("Invalid Mode:")
    
    full_mode=""

    if user_mode=="e":

        full_mode="encrypt"
    else:
        full_mode="decrypt"
    
    text_message=input(f"Enter the text to {full_mode}:").upper()
    return (user_mode, text_message)


def encrypt(text_message, shift_value):
    plain_text=""
    for string in text_message:
        if string != " ":

            plain_text+=chr((ord(string) + shift_value - 65) % 26 +65)
        else:
            plain_text += " "
    return plain_text


def decrypt(text_message, shift_value):
    plain_text = ""
    for string in text_message:
        if string !=" ":

            plain_text+=chr((ord(string) - shift_value - 65) % 26 +65)
        else:
            plain_text += " "
    return plain_text

def is_file(filename):
    return os.path.isfile(filename)

def write_message(messages):

    with open("results.txt","w") as f:
        for text_message in messages:
            f.write(text_message)

def message_or_file():

    while True:

        file_or_console= input("Would you like to read from a file (f) or the console (c)? f:").lower()
        if file_or_console=="c" or file_or_console=="f":
            break
        print("Invalid option")

    if file_or_console=="c":
        message_to_cypher=enter_message()
        return (message_to_cypher[0], message_to_cypher[1],None)
    
    while True:

        file_name=input("Enter the filename:")
        if is_file(file_name):
            break
        print("Invalid filename")

    while True:
        user_mode= input("Would you like to encrypt (e) or decrypt (d):").lower()
        if user_mode=="e" or user_mode=="d":
            return(user_mode,None,file_name)
        
        print("Invalid Mode")

def process_file(filename,user_mode):

    ceaser_msgs=[]
    with open(filename) as f:
        for line in f:
            line=line.upper()

            if user_mode=="e":
                ceaser_msgs.append(encrypt(line, SELECTED_SHIFT))
            else:
                result=decrypt(line,SELECTED_SHIFT)
                ceaser_msgs.append(result)
    return ceaser_msgs
    

def main():
     
     while True:
        global SELECTED_SHIFT
        user_selected_option=message_or_file()

        while True:
            shift_number=input("Enter the shift number:")
            if shift_number.isdigit():
                SELECTED_SHIFT=int(shift_number)
                break
            print("Invalid shift")
        if user_selected_option[1]==None:

            cypher=process_file(user_selected_option[-1],user_mode=user_selected_option[0])
            write_message(cypher)
            print("The result is written to results.txt file")
            
        else:
            if user_selected_option[0]=="e":
                print(encrypt(user_selected_option[1] ,SELECTED_SHIFT))
            else:
                print(decrypt(user_selected_option[1] ,SELECTED_SHIFT))

        another_message=input("Would you like to encrypt or decrypt another message? (y/n): ").lower()

        if another_message == "n":
            break
main()






    