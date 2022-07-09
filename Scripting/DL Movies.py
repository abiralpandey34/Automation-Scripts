import pyautogui
import time

movie = input('which movie do you want me to download ')

pyautogui.hotkey('winleft','m') #show desktop
time.sleep(0.5)

pyautogui.hotkey('winleft','1') #opens browser
time.sleep(2)

pyautogui.hotkey('ctrl','t')    #open a new tab
pyautogui.hotkey('ctrl','l')    #To click on search Bar


#typing down the website address
pyautogui.typewrite('https://www.1337x.to/home/')
pyautogui.press('enter')


time.sleep(4)
pyautogui.moveTo(1000,150)
pyautogui.click()
pyautogui.typewrite(movie)
pyautogui.press('enter')


time.sleep(5)
#choosin movie quality
pyautogui.moveTo(242,404)
pyautogui.click()

time.sleep(5)#load hudai xa

pyautogui.click(pyautogui.locateCenterOnScreen('D:\\magnet.png'))#magnet ma click garni

time.sleep(1)
pyautogui.moveTo(786,187)  #qbittorrent bata open garne vanera OK garni
pyautogui.click()


pyautogui.moveTo(296,310)  #download sequentially
pyautogui.click()

time.sleep(3)
pyautogui.moveTo(1070,606) #Start downloading
pyautogui.click()





















