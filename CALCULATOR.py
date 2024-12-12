class Calculator:
    def __init__(self):
        print("WELCOME TO THE CALCULATOR PROGRAM")
    def UserValues(self):
        number_1=float(input("ENTER TWO NUMBERS:"))
        number_2=float(input("ENTER TWO NUMBERS:"))
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
loop="Y"
C=Calculator()
while(loop!="N"):
    try:

            result=C.ChoiceEvaluation()
            print("RESULT OF THE OPERATION IS",result)
    except Exception as e:
        print("AN ERROR OCCUR PLS TRY AGAIN.....")
    finally:
        loop=input("DO YOU WISH TO CONTINUE (Y/N)").upper()
print("THANKYOU VISIT AGAIN")