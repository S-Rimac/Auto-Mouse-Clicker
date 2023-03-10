import pyautogui
import keyboard
import threading

clicking = False

def start_clicking():
    while True:
        if clicking:
            pyautogui.click(button='left')
            pyautogui.sleep(0.001)
        else:
            pyautogui.sleep(0.001)

def on_press_t(click):
    global clicking
    clicking = not clicking

keyboard.on_press_key("t", on_press_t)

click_thread = threading.Thread(target=start_clicking)
click_thread.start()

keyboard.wait()
