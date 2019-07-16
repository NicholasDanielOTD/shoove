#Shoove a lightweight FLOSS application to take screenshots by dragging and dropping

import keyboard
import os
import configparser
import pyautogui
import mouse

#Init variables
IMAGES_PATH = "None"
PICTURE_HOTKEY = "None"
CLOSE_HOTKEY = "None"
x1=x2=y1=y2=None

#Check for config
config = configparser.ConfigParser()
if os.path.isfile(os.getcwd()+"/cfg.ini"):
    print("Configuration found!\nLoading configuration...")
    config.read('cfg.ini')
    
else:
    print("Configuration not found!\nGenerating configuration...")
    pathin = input("Please enter the path you wish to save images to: ")
    while not os.path.exists(pathin):
        pathin = input("Sorry that directory does not exist, please enter an existing directory: ")
    config['KEYBINDS'] = {'PICTURE_HOTKEY': 'ctrl+shift+4', 'CLOSE_HOTKEY': 'ctrl+shift+escape'}
    config['PATH'] = {'IMAGES_PATH':pathin}
    with open('cfg.ini', 'w') as configfile:
        config.write(configfile)

#Load hotkeys
PICTURE_HOTKEY = config['KEYBINDS']['PICTURE_HOTKEY']
CLOSE_HOTKEY = config['KEYBINDS']['CLOSE_HOTKEY']



print("Ready to take screenshots!")

def takeScreenshot():
    print("Taking a screenshot")
    keyboard.remove_hotkey(takeScreenshot)
    mouse.on_button(print, args=['yes'], buttons=('left'), types=('down'))
    mouse.on_button(setFirstCursorPosition, buttons=('left'), types=('down'))
    keyboard.on_press_key('escape', cancelScreenshot)



def setFirstCursorPosition():
    print("Setting first position")
    x1 = pyautogui.position()[0]
    y1 = pyautogui.position()[1]

def setSecondCursorPosition():
    print("Setting second position")
    x2, y2 = pyautogui.position()
    mouse.unhook_all()
    keyboard.remove_hotkey(cancelScreenshot)

    print(x1,y1)
    
def cancelScreenshot():
    print("Cancelling screenshot")
    x1=x2=y1=y2=1
    
def shutdown():

    keyboard.unhook_all_hotkeys()
    exit()
    
    


keyboard.add_hotkey(PICTURE_HOTKEY, takeScreenshot)
keyboard.add_hotkey(CLOSE_HOTKEY, shutdown)


input()

