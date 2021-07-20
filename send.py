import time
from pynput import keyboard
#pip install pynput
#pip install keyboard

time.sleep(3)

m_keyboard = keyboard.Controller()
f = open("msg.txt",encoding='utf-8')
line = f.readline()
while line:
    m_keyboard.type(line)
    m_keyboard.press(keyboard.Key.enter)
    m_keyboard.release(keyboard.Key.enter)
    line = f.readline()
f.close()
