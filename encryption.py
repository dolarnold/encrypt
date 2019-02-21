from sys import exit
while True:
    choice = input("\nDo you want to encrypt or decrypt the message?\nEnter 1 to encrypt.\nEnter 2 to decrypt.\nEnter  0 to exit the program.\n>>")
    if choice == '1':
        message = input("enter message for encryption:")
        for i in range(0,len(message)):
            result = result + chr(ord(message[i]) - 2)
            print(result + '\n')
    elif choice == '2':
        message = input("\nenter message for decryption:")
        result  = ([ord(i) for i in message])
        print(result)
            #result =''
    elif choice == '0':
        print("Closing program")
        break
            
            