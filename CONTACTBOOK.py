class ContactBook:
    phonebook={}
    def AddContact(self,count):
        for i in range(0,count):
            name=input("Enter Name:")
            phone=int(input("ENTER PHONE NUMBER:"))
            email=input("ENTER THE EMAIL ADDRESS:")
            address=input("ENTER ADDRESS")
            self.phonebook[phone]=[name,email,address]
            print("CONTACT ADDED SUCCESSFULLY")

    def ViewContacts(self):
        i=0
        for key,value in self.phonebook.items():
            name,email,address=value
            print(f"CONTACT LIST {i}:\n name:{name}\n phone:{key}\n email:{email}\n address:{address}")
            i+=1

    def SearchContact(self):
        key=0
        ch=int(input("DO YOU WANT TO SEARCH USING NAME(1) OR PHONE(2)\nEnter YOUR CHOICE:"))
        if(ch==1):
            name=input("ENTER NAME TO FIND:")
            for keys,value in self.phonebook.items():
                if (name in value):
                    key=keys
                    break
        elif(ch==2):
            phone=int(input("ENTER A PHONE NUMBER TO SEARCH"))
            for keys in self.phonebook.keys():
                if(phone == keys):
                    key=keys
                    break
        name,email,address=[*self.phonebook[keys]]
        print(f"NAME:{name}\nphone:{key}\nEMAIL:{email}\nADDRESS:{address}")
                        

CB=ContactBook()
count=int(input("Enter number of contact to be add"))
CB.AddContact(count)
CB.ViewContacts()
CB.SearchContact()