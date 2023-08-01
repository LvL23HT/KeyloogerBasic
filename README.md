# v2.0 by dEEpEst 

# Keyboard Logger with Log Sending to Discord 

This Python script uses the `pynput.keyboard` and `requests` modules to capture keystrokes from the user and send them to a Discord webhook when a specific key is pressed.

Here is a detailed explanation of each part of the script:

## Dependencies:
```
import requests
from pynput.keyboard import Key, Listener
```
The script imports the `requests` module, which allows it to send HTTP requests. It also imports `Key` and `Listener` from `pynput.keyboard`, which are used for capturing keyboard input.

## Global variables:
```
LOG_FILE = 'log.txt'
WEBHOOK_URL = 'YOUR_WEBHOOKS_API_HERE'
```
`LOG_FILE` is the name of the file where the keystrokes will be stored, and `WEBHOOK_URL` is the URL of the Discord webhook where the log file will be sent when the F12 key is pressed.

## Functions 

### Function write_file(key):
This function is called each time a key is pressed. It processes the key press, converts it into a string, and writes it to the log file.

### Function send_log():
This function opens the log file in binary mode, prepares it for sending as a file attachment, and then sends it to the Discord webhook URL using a POST request. It will print the HTTP response status code if the request is successful, or print an error message if it fails.

### Function on_release(key):
This function is called each time a key is released. If the key released is F12, it will call the `send_log()` function to send the log file, and then return False to stop the key listener.

## Listener:

```
with Listener(on_press=write_file, on_release=on_release) as listener:
    listener.join()
```

This starts a new `Listener` that listens for key press and key release events. It calls the `write_file(key)` function when a key is pressed and the `on_release(key)` function when a key is released.

## Disclaimer
This script was created for educational purposes and is intended to demonstrate how key logging and Discord webhook functionalities can be implemented in Python.

### IMPORTANT:

The misuse of this script could lead to the invasion of privacy or unauthorized data access, which is illegal and unethical. It's critical that you only use or modify this code if you understand the implications and potential consequences, and you have obtained explicit permission from the relevant parties.

This code should never be used for malicious purposes. The creator of this code does not condone or support any form of unauthorized or illegal use.

By using or modifying this code, you agree to assume all responsibility for any resulting consequences, and you acknowledge that the code creator cannot be held responsible for any misuse or data breaches that may occur as a result of using this code.

## License
This project is licensed under the *MIT License*. Please see the LICENSE file in the root of the repository for the full license text.

By using or modifying this code, you are agreeing to comply with the terms and conditions of this license. The MIT License is a permissive open source license that allows for reuse of the licensed material under certain conditions, primarily that the original copyright notice and disclaimer are retained and included with any distribution or publication of the material.

## Link:
Visit [Level23HackTools](https://level23hacktools.com) for more information on hacking and computer security.

Enjoy using the app!

---
# v1.0 by dEEpEst 

# KeyloogerBasic

Keylogger written in Python

## Description:

This code is a simple keylogger that records the keys you press on your keyboard and keep them in a file called 'log.txt'. Below is what each part of the code does:

IMPORT PYNPUT: This imports the Pynput module, which is a Python library to control and monitor the keyboard and mouse.

from pynput.keyboard import key, listener: This matters the specific Key and Listener classes of pynput.keyboard. Key is an enumeration that represents the special keys (such as function keys, shift, Ctrl, etc.), and Listener is a class that allows your program to listen to keyboard events.

Def on_press (Key): This is a function called every time you press a key on the keyboard. Take a single argument, which is the key that was pressed.

Write_file (Key): This function writes the key pressed in the 'log.txt' file. The file opens in addition mode ('A'), which means that the new keys will be added at the end of the file instead of overwriting the file. The pressured key becomes a chain and the quotes are deleted before writing it in the file. If an error occurs when writing the file, an error message is printed.

Def on_release (key): This is another function that is called every time you release a key on the keyboard. If the key that was released is F12, the function returns false, which stops the listener and ends the program.

with listener (on_press = on_press, on_release = on_release) as listener: this starts a listener that calls the on_press and on_ functions every time a key is pressed or released, respectively. The listener runs in a loop until it stops (for example, when the F12 key is released).

# Website:
https://level23hacktools.com/hackers/profile/1-deepest
