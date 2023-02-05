import pyautogui
import time

result = pyautogui.confirm(text="Do you want to shutdown?", buttons=('Yes','No'))

if(result=='Yes'):
    pyautogui.hotkey('win')
    time.sleep(0.5)
    pyautogui.hotkey('up')
    time.sleep(0.5)
    pyautogui.hotkey('right')
    time.sleep(0.5)
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')
else:
    pyautogui.alert(text='Bye')