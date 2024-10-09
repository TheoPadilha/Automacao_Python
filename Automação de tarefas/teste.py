import pyautogui as py
import time

py.PAUSE = 1
py.press('win')
py.write('opera')
py.press('enter')

py.write('https://www.youtube.com')
py.press('enter')
py.PAUSE = 4
py.click(x=928, y=125)
py.write('coringa')
py.PAUSE = 0.5
py.press('enter')


