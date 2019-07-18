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
    config['KEYBINDS'] = {'PICTURE_HOTKEY': 'ctrl+shift+4', 'CLOSE_HOTKEY': 'ctrl+5'}
    config['PATH'] = {'IMAGES_PATH':pathin}
    with open('cfg.ini', 'w') as configfile:
        config.write(configfile)

#Load hotkeys
PICTURE_HOTKEY = config['KEYBINDS']['PICTURE_HOTKEY']
CLOSE_HOTKEY = config['KEYBINDS']['CLOSE_HOTKEY']



print("Ready to take screenshots!")

class Screenshot:

	def __init__(self):
		self.x1=self.y1=self.x2=self.y2=None
	
	def takeScreenshot(self):
		print("Taking a screenshot")
		keyboard.remove_hotkey(s.takeScreenshot)
		mouse.on_button(self.setFirstCursorPosition, buttons=('left'), types=('down'))
		mouse.on_button(self.setSecondCursorPosition, buttons=('left'), types=('up'))
		keyboard.add_hotkey('escape', s.cancelScreenshot)

	def setFirstCursorPosition(self):
		print("Setting first position")
		self.x1 = pyautogui.position()[0]
		self.y1 = pyautogui.position()[1]

	def setSecondCursorPosition(self):
		print("Setting second position")
		self.x2 = pyautogui.position()[0]
		self.y2 = pyautogui.position()[1]
		mouse.unhook_all()
		keyboard.remove_hotkey('escape')
		keyboard.add_hotkey(PICTURE_HOTKEY, s.takeScreenshot)
		
		self.captureScreen()
		
	def cancelScreenshot(self):
		print("Cancelling screenshot")
		mouse.unhook_all()
		keyboard.add_hotkey(PICTURE_HOTKEY, s.takeScreenshot)
		keyboard.remove_hotkey(s.cancelScreenshot)
    
	def captureScreen(self):
		print(self.x1,self.y1,self.x2,self.y2)
	
	
def shutdown():
	keyboard.unhook_all_hotkeys()
	exit()
    
    
s = Screenshot()
	
keyboard.add_hotkey(PICTURE_HOTKEY, s.takeScreenshot)
keyboard.add_hotkey(CLOSE_HOTKEY, shutdown)


input()


