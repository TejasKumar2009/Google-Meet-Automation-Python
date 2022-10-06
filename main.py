#Automating the Google Meet

#importing some modules
import pyautogui as pg #Docs - https://pyautogui.readthedocs.io/en/latest/
import webbrowser
import time

#Main Program Starts from here!!
print("VERSION 1.0\n")
print("This Software is only for automate google meet\n")
print('''Note - The software is do not support 'change your account' so
please enter the link with your account ex(authuser=1)\n''')
print("Program Strats in 3 seconds")
time.sleep(3)

#Inputs
link_inp = input("Enter the meet code https://meet.google.com/")
open_link = f"https://meet.google.com/{link_inp}"

print("Your program Join the class after 3 seconds...")
time.sleep(3)

#Opening Chrome
pg.moveTo(200, 1050)
pg.click()
time.sleep(1)
pg.write("Chrome")
time.sleep(1)
pg.keyDown("enter")


#Writing link on chrome
time.sleep(3)
pg.write(open_link)
time.sleep(3)
pg.keyDown("enter")

#Off mic and camera
time.sleep(5)
pg.hotkey("ctrl", "d")
pg.click()
time.sleep(3)
pg.hotkey("ctrl", "e")
pg.click()

#Join the meeting
time.sleep(3)
pg.moveTo(1300, 600)
pg.click()



