import random
list=["ROCK","PAPER","SCISSOR"]
ACCEPTED=[("PAPER","ROCK"),("ROCK","SCISSOR"),("SCISSOR","PAPER")]
TIE=[("ROCK","ROCK"),("PAPER","PAPER"),("SCISSOR","SCISSOR")]
loop="Y"
score=0
while(loop!="N"):
    for i in range(0,3):
        print(f"{i}.{list[i]}")
    player_choice=list[int(input("Enter your choice:"))]
    random_choice=random.choice(list)
    print(f"YOUR CHOICE:{player_choice}\nRANDOM CHOICE:{random_choice}")
    temp=(player_choice,random_choice)
    if (temp in ACCEPTED):
        score+=1
        print("YOU WIN")
    elif(temp in TIE):
        score=score
        print("IT'S A TIE")
    else:
        print("YOU LOST....")
        print(f"TOTAL SCORE:{score}")
        score=0
        loop=input("DO YOU WISH TO CONTINUE (Y/N)").upper()
    