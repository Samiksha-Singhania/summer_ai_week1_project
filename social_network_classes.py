# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
        
    ## For more challenge try this
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass

    def create_account(self):
        #implement function that creates account here
        name = input("Enter name: ")
        age = input("Enter age: ")
        email = input("Enter email: ")
        p1 = Person(name,age,email)
        print(p1.id)
        self.list_of_people.append(p1)
        
    def which_account(self,name):
        for user in  self.list_of_people:
            if user.id == name:
                return user


class Person:
    def __init__(self, name, age, email):
        self.id = name
        self.year = age
        self.email = email
        self.friendlist = []
        self.messages = []
        self.blocked_friends = []

    def add_friend(self, name):
        #implement adding friend. Hint add to self.friendlist
        if name not in self.friendlist:
            self.friendlist.append(name)
        

    def view_friends(self):
        print (self.friendlist)
    
    def block_friend(self, name):
        if name in self.friendlist:
            self.friendlist.remove(name)
            self.blocked_friends.append(name)
        

    def send_message(self, person, message, mysocialnetwork):
        #if person in self.friendlist:
        for user in  mysocialnetwork.list_of_people:
            if user.id == person:
                print("User: ")
                print(user)
                user.messages.append(message)
 
    def view_message(self):
        print(self.messages)

    def changename(self):
        n = input("Add new name: ")
        print("Your new name is " + n)
        self.id = n

    def changeage(self):
        a = input("Add new age: ")
        print("Your new age is " + a)
        self.year = a

    def changeemail(self):
        e = input("Add new email: ")
        print("Your new email is " + e)
        self.email = e