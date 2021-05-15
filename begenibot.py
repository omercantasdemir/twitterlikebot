import time
import pyautogui
import os

while True:
    try:
        location= pyautogui.locateOnScreen(os.getcwd()+'/twitterlikebot/tus.png') #relative location for like button
        if location!=None: #a little bug sorted out, important step
            pyautogui.click(location)
    except:
        pyautogui.press('pagedown')
    finally:
        pyautogui.PAUSE =0.3
    pyautogui.scroll(-100)