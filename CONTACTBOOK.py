class ContactBook:
    phonebook={}
    def displine(self):
        print("===================================================")
    def AddContact(self,count):
        for i in range(0,count):
            self.displine()
            name=input("Enter Name:").upper()
            phone=int(input("ENTER PHONE NUMBER: "))
            email=input("ENTER THE EMAIL ADDRESS: ").upper()
            address=input("ENTER ADDRESS: ").upper()
            self.phonebook[phone]=[name,email,address]
            self.displine()
            print("CONTACT ADDED SUCCESSFULLY")

    def ViewContacts(self,key=None):
        self.displine()
        if (key is None):
            i=0
            for key,value in self.phonebook.items():
                name,email,address=value
                print(f"CONTACT LIST {i}:\n name:{name}\n phone:{key}\n email:{email}\n address:{address}")
                i+=1
                self.displine()
        elif key in self.phonebook:
            name,email,address=[*self.phonebook[key]]
            print(f"NAME:{name}\nphone:{key}\nEMAIL:{email}\nADDRESS:{address}")
            self.displine()

    def SearchContact(self):
        ch=int(input("DO YOU WANT TO SEARCH USING NAME(1) OR PHONE(2)\nEnter YOUR CHOICE: "))
        if(ch==1):
            self.displine()
            name=input("ENTER NAME TO FIND: ").upper()
            for keys,value in self.phonebook.items():
                if (name in value):
                    key=keys
                    return(key)
        elif(ch==2):
            self.displine()
            phone=int(input("ENTER A PHONE NUMBER TO SEARCH: "))
            for keys in self.phonebook.keys():
                if(phone == keys):
                    key=keys
                    return(key)
    def UpdateContact(self):
        key=self.SearchContact()
        self.displine()
        print("ENTER NONE FOR NOCHANGE FOR NUMBER USE 0 ")
        self.displine()
        name=input("Enter Name:").upper()
        phone=int(input("ENTER PHONE NUMBER: "))
        email=input("ENTER THE EMAIL ADDRESS: ").upper()
        address=input("ENTER ADDRESS: ").upper()
        self.displine()
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

CB = ContactBook()  # Create one instance of ContactBook to persist contacts
while True:
    count = int(input("Enter number of contacts to be added: "))
    CB.AddContact(count)
    ch = input("DO YOU WISH TO VIEW ALL CONTACTS (Y/N): ").upper()
    if ch == "Y":
        CB.ViewContacts()
    ch = input("DO YOU WISH TO SEARCH CONTACTS (Y/N): ").upper()
    if ch == "Y":
        key = CB.SearchContact()
        CB.ViewContacts(key)
    ch = input("DO YOU WISH TO UPDATE CONTACTS (Y/N): ").upper()
    if ch == "Y":
        CB.UpdateContact()
    ch = input("DO YOU WISH TO DELETE CONTACTS (Y/N): ").upper()
    if ch == "Y":
        CB.DeleteContact()
    loop = input("DO YOU WISH TO CONTINUE (Y/N): ").upper()
    if(loop=="N"):
        break