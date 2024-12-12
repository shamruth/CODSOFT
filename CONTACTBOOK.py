class ContactBook:
    phonebook={}
    def AddContact(self,count):
        for i in range(0,count):
            name=input("Enter Name:").upper()
            phone=int(input("ENTER PHONE NUMBER: "))
            email=input("ENTER THE EMAIL ADDRESS: ").upper()
            address=input("ENTER ADDRESS: ").upper()
            self.phonebook[phone]=[name,email,address]
            print("CONTACT ADDED SUCCESSFULLY")

    def ViewContacts(self,key=None):
        if (key is None):
            i=0
            for key,value in self.phonebook.items():
                name,email,address=value
                print(f"CONTACT LIST {i}:\n name:{name}\n phone:{key}\n email:{email}\n address:{address}")
                i+=1
        elif key in self.phonebook:
            name,email,address=[*self.phonebook[key]]
            print(f"NAME:{name}\nphone:{key}\nEMAIL:{email}\nADDRESS:{address}")

    def SearchContact(self):
        ch=int(input("DO YOU WANT TO SEARCH USING NAME(1) OR PHONE(2)\nEnter YOUR CHOICE: "))
        if(ch==1):
            name=input("ENTER NAME TO FIND: ").upper()
            for keys,value in self.phonebook.items():
                if (name in value):
                    key=keys
                    return(key)
        elif(ch==2):
            phone=int(input("ENTER A PHONE NUMBER TO SEARCH: "))
            for keys in self.phonebook.keys():
                if(phone == keys):
                    key=keys
                    return(key)
    def UpdateContact(self):
        key=self.SearchContact()
        print(key)
        print("ENTER NONE FOR NOCHANGE FOR NUMBER USE 0 ")
        name=input("Enter Name:").upper()
        phone=int(input("ENTER PHONE NUMBER: "))
        email=input("ENTER THE EMAIL ADDRESS: ").upper()
        address=input("ENTER ADDRESS: ").upper()
        self.phonebook[key][0]=name if name!="NONE" else self.phonebook[key][0]
        self.phonebook[key][1]=email if email!="NONE" else self.phonebook[key][1]
        self.phonebook[key][2]=address if address!="NONE" else self.phonebook[key][2]
        if phone != 0 and phone != key:
            self.phonebook[phone] = self.phonebook.pop(key)  # Change the key
            key = phone  # Update the key to the new phone number
            print("UPDATED CONTACT:")
        self.ViewContacts(key)
    def DeleteContact(self):
        key=self.SearchContact()
        del self.phonebook[key]
        print("DISPLAYING ALL CONTACTS AFTER DELETING")
        self.ViewContacts()

    
                        
loop="Y"
while(loop!="N"):
    CB=ContactBook()
    count=int(input("Enter number of contact to be add"))
    CB.AddContact(count)
    ch=input("DO YOU WISH TO VIEW ALL CONTACTS(Y/N)").upper()
    CB.ViewContacts()if ch=="Y" else ch="N"
    ch=input("DO YOU WISH TO SEARCH CONTACTS(Y/N)").upper()
    if(ch=="Y"):
        key=CB.SearchContact()
        CB.ViewContacts(key)
    ch=input("DO YOU WISH TO UPDATE CONTACTS(Y/N)").upper()
    CB.UpdateContact() if ch=="Y" else ch="N"
    ch=input("DO YOU WISH TO DELETE CONTACTS(Y/N)").upper()
    CB.DeleteContacts() if ch=="Y" else ch="N"
    loop=input("DO YOU WISH TO CONTINUE(Y/N)")