import random,string
def Passcode_generator(choice,length):
    if(choice ==1):
        combination=string.digits
    elif(choice == 2):
        combination=string.ascii_letters
    elif(choice == 3):
        combination=string.ascii_letters+string.digits
    passcode=''.join(random.choices(combination,k=length))
    return(passcode)
def UserInput():
    print("==============================================================")
    length=int(input("Enter length of your passcode:"))
    print("==============================================================")
    choice=int(input(" 1.NUMBERS ONLY \n 2.LETTERS ONLY \n 3.LETTERS and NUMBERS \nENTER YOUR COMPLEXITY:"))
    print("==============================================================")
    return(Passcode_generator(choice,length))
print("WELCOME TO PASSWORD GENERATOR")
while True:
    try:
        passcode=UserInput()
        print("==============================================================")
        print("THE GENERATED PASSWORD IS:",passcode)
        print("==============================================================")
    except Exception as e:
        print(e)
        print("TRY AGAIN")
        continue
    loop=input("DO YOU WISH TO GENERATE ANOTHER PASSCODE (Y/N)").upper()
    if(loop=="N"):
        break
