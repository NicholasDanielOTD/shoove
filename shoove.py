#Shoove a lightweight FLOSS application to take screenshots by dragging and dropping

import keyboard
import os
import configparser

#Init variables
IMAGES_PATH = "None"
PICTURE_HOTKEY = "None"
CLOSE_HOTKEY = "None"


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

PICTURE_HOTKEY = config['KEYBINDS']['PICTURE_HOTKEY']
CLOSE_HOTKEY = config['KEYBINDS']['CLOSE_HOTKEY']

print("Ready to take screenshots!")

def takeScreenshot():

    print("click!")



    
    
    
    
def shutdown():

    keyboard.unhook_all_hotkeys()
    exit()
    
    


    



keyboard.add_hotkey(PICTURE_HOTKEY, takeScreenshot)
keyboard.add_hotkey(CLOSE_HOTKEY, shutdown)


