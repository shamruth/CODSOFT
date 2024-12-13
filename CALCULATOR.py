class Calculator:
    def __init__(self):
        print("WELCOME TO THE CALCULATOR PROGRAM")
    def UserValues(self):
        number_1=float(input("ENTER A NUMBERS:"))
        number_2=float(input("ENTER A NUMBERS:"))
        choice=input("\nADDITION(+)\nSUBRACTION(-)\nMULTIPLICATION(*)\nDIVISION(/)\nMODULO(%)\nENTER YOUR CHOICE:")
        return(number_1,number_2,choice)
    def ChoiceEvaluation(self):
        number_1,number_2,choice=self.UserValues()
        if(choice=="+"):
            return(number_1+number_2)
        elif(choice=="-"):
            return(number_1-number_2)
        elif(choice=="*"):
            return(number_1*number_2)
        elif(choice=="/"):
            return(number_1/number_2)
        elif(choice=="%"):
            return(number_1%number_2)
C=Calculator()
while True:
    try:
            result=C.ChoiceEvaluation()
            print("========================================")
            print("RESULT OF THE OPERATION IS",result)
            print("========================================")
    except Exception as e:
        print(e)
        print("AN ERROR OCCUR PLS TRY AGAIN.....")
        continue
    loop=input("DO YOU WISH TO CONTINUE (Y/N)").upper()
    if(loop=="N"):
        break
print("THANKYOU VISIT AGAIN")