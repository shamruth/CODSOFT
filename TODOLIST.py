TODO=[]
def add():
     task=(input("ENTER NEW TASK: ")).upper()
     TODO.append([task])
     print("task added successfully")
def track():
     i=0
     for task in TODO:
          print("+++++++++++++++++++++++++++++++++++++++")
          print(f"{i}  {str(*task)+" "+"INCOMPLETE"}")
          print("+++++++++++++++++++++++++++++++++++++++")
          i+=1
def update():
     track()
     ch=int(input("ENTER TASK TO UPDATE AS COMPLETED: "))
     print(str(*TODO[ch])+" "+"COMPLETED")
     delete(ch)
def delete(ch=None):
    if(ch is None):
        track()
        ch=int(input("ENTER TASK TO DELETE: "))
        del(TODO[ch])
    else:
         del(TODO[ch])
         
if __name__=='__main__':
        print("WELCOME TO TO-DO LIST APPLICATION")      
        while True:
            print("1.ADD TASK")
            print("2.TRACK TASK")
            print("3.UPDATE TASK")
            print("4.DELETE TASK")
            print("5.QUIT")
            print("================================================")
            choice=int(input("Enter Your Choice: "))
            if(choice==1):
                add()
            elif(choice==2):
                track()
            elif(choice==3):
                update()
            elif(choice==4):
                delete()
            elif(choice==5):
                break
            else:
                print("INVALID INPUT TRY AGAIN")
