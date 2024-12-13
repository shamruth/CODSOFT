import random
list=["ROCK","PAPER","SCISSOR"]
ACCEPTED=[("PAPER","ROCK"),("ROCK","SCISSOR"),("SCISSOR","PAPER")]
score=0
while True:
    for i in range(0,3):
        print(f"{i}.{list[i]}")
    player_choice=int(input("Enter your choice:"))
    random_choice=random.choice(list)
    print("===========================================================")
    print(f"YOUR CHOICE:{list[player_choice]}\nRANDOM CHOICE:{random_choice}")
    print("===========================================================")
    temp=(list[player_choice],random_choice)
    if (temp in ACCEPTED):
        score+=1
        print("YOU WIN")
        print("===========================================================")
    elif(list[player_choice] == random_choice):
        score=score
        print("IT'S A TIE")
        print("===========================================================")
    else:
        print("YOU LOST....")
        print(f"TOTAL SCORE:{score}")
        print("===========================================================")
        score=0
        loop=input("DO YOU WISH TO CONTINUE (Y/N)").upper()
        if(loop=="N"):
            break