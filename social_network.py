#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_ui



#Create instance of main social network object
ai_social_network = SocialNetwork()
fakeperson = Person("Mary", 34, "mary12@gmail.com")
#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu ")
            ai_social_network.create_account()

        elif choice == "2":
            #Handle inner menu here
            cuser = None
            user_name = input("Enter name ")
            cuser = ai_social_network.which_account(user_name)
            inner_menu_choice = social_network_ui.manageAccountMenu()


            while True:
                if inner_menu_choice == "7":
                    break
                
                elif inner_menu_choice == "1":
                    edit_menu_details_choice = social_network_ui.editdetails()
                    while True:
                        if edit_menu_details_choice == "1":
                            cuser.changename()
                            break
                        if edit_menu_details_choice == "2":
                            cuser.changeage()
                            break
                        if edit_menu_details_choice == "3":
                            cuser.changeemail()
                            break
                        if edit_menu_details_choice == "4":
                            edit_menu_details_choice = social_network_ui.manageAccountMenu()

                elif inner_menu_choice == "2":
                    f = input("which friend do you want to add? ")
                    # print(cuser.id)
                    cuser.add_friend(f)
                    print(" You added friend " + f)
                    break

                elif inner_menu_choice == "3":
                  print("This is your friend list")
                  cuser.view_friends()
                  break

                elif inner_menu_choice == "4":
                    print("You recieved a message")
                    cuser.view_message()
                    break
                
                elif inner_menu_choice == "5":
                    b = input("which friend do you want to block? ")
                    # print(cuser.id)
                    cuser.block_friend(b)
                    print(" You blocked friend " + b)
                    break 
      
                elif inner_menu_choice == "6":
                    m = input("Who do you want to send message to? ")
                    sm = input("What message do you want to send? ")
                    sn = ai_social_network
                    cuser.send_message(m,sm,sn)
                    print("You sent a message")
                    break
                else:
                    inner_menu_choice = social_network_ui.manageAccountMenu()

        elif choice == "3":
            print("Thank you for visiting. Goodbyeb User!")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        
