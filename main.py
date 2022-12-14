from user import User 

loginPreference = input(""" 
                          WELCOME TO IZTECH BANK
                        --------------------------
                        1. SIGN IN TO IZTECH BANK
                        2. LOGIN TO IZTECH BANK

: """)

if loginPreference == "1": # Sign
    username = input("Please enter your username:\n")
    email = input("Please enter your email:\n")
    password = input("Please enter your password:\n")
    new_user = User(None, username, password, email)
    new_user.save_user()
    print(f"""
                    WELCOME TO IZTECH BANK
                    --------------------------
                    YOUR NEW ID -> {new_user.user_id}
    """)

elif loginPreference == "2": # Login
  entered_id = input("Please enter your ID:\n")
  entered_password = input("Please enter your password:\n")
  allow_user = User.check_id_password(None, entered_id, entered_password)
  allow = allow_user[0]
  user_info = allow_user[1]

  # print(allow)
  if allow == True:
    user1 = User(user_info[0], user_info[1], user_info[2], user_info[3], user_info[4])
    action = input(f"""

                                 WELCOME {user1.username}

                    PLEASE CHOOSE THE NUMBER OF THE ACTİON YOU WANT
                    -----------------------------------------------
                    
                            YOUR BUDGET ==> {user1.balance}
                    
                    1. TO DEPOSİT MONEY
                    2. TO WİTHDRAWAL MONEY
                    3. TO CHANGE EMAİL
                    
                    """)

    if action == "1":
      user1.deposit()
      print(f"YOUR NEW BALANCE ==>{user1.balance}")

    elif action == "2":
      user1.withdrawal()
      print(f"YOUR NEW BALANCE ==>{user1.balance}")

    elif action == "3":
      user1.change_email()
    
    
    user1.final_func()
  
  elif allow == False:
    print("          ---->  WRONG ID OR PASSWORD  <----\n\n\n")
