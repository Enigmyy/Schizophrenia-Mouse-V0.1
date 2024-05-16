import pyautogui as pag 
import random 
import time
 
#Loop to leep sript running 
while True: 
    x = random.randint(700,800) #Random X 
    y = random.randint(300,700) #Random y
    speed = random.uniform(0.5, 1.5)
    delay = random.uniform(1, 3)
    
    pag.moveTo(x,y,speed) #Cursor move speed 
    pag.click() #Adds random clicks while moving
    time.sleep(2) #Pause script before nect interation