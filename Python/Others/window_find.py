import pygetwindow as gw
import keyboard

vlc_window = gw.getWindowsWithTitle ("Bones in the Ocean") [0]
print (vlc_window)
vlc_window.activate()
keyboard.press_and_release ("space")