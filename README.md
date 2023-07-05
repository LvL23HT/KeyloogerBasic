# KeyloogerBasic

Keylogger written in Python

# Description:

This code is a simple keylogger that records the keys you press on your keyboard and keep them in a file called 'log.txt'. Below is what each part of the code does:

IMPORT PYNPUT: This imports the Pynput module, which is a Python library to control and monitor the keyboard and mouse.

from pynput.keyboard import key, listener: This matters the specific Key and Listener classes of pynput.keyboard. Key is an enumeration that represents the special keys (such as function keys, shift, Ctrl, etc.), and Listener is a class that allows your program to listen to keyboard events.

Def on_press (Key): This is a function called every time you press a key on the keyboard. Take a single argument, which is the key that was pressed.

Write_file (Key): This function writes the key pressed in the 'log.txt' file. The file opens in addition mode ('A'), which means that the new keys will be added at the end of the file instead of overwriting the file. The pressured key becomes a chain and the quotes are deleted before writing it in the file. If an error occurs when writing the file, an error message is printed.

Def on_release (key): This is another function that is called every time you release a key on the keyboard. If the key that was released is F12, the function returns false, which stops the listener and ends the program.

with listener (on_press = on_press, on_release = on_release) as listener: this starts a listener that calls the on_press and on_ functions every time a key is pressed or released, respectively. The listener runs in a loop until it stops (for example, when the F12 key is released).

# Website:
https://level23hacktools.com/hackers/profile/1-deepest
