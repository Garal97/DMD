import os
import webbrowser
import keyboard
import time

webbrowser.open("https://www.youtube.com/watch?v=hWPPD5ww0eA")
time.sleep (5)
keyboard.press_and_release ('space')
webbrowser.open ("https://www.youtube.com/watch?v=nOzeJzikKjc", autoraise=False)
time.sleep (1)
keyboard.press_and_release ("windows+m")
keyboard.press_and_release ("atl+tab")
keyboard.press ("alt")
keyboard.press_and_release ("tab")
keyboard.press_and_release ("tab")
keyboard.release ("alt")