import sys
import json
import socket
import threading
import random
import time
import mutex

from pythonchord.address import Address, inrange
from pythonchord.remote import Remote
from pythonchord.settings import *
from network import *
from pythonchord.chord import *

def generate_id(x, y, range):
    return int(int(x)/range*360/range+int(y)/range)

class Taxi(object):
    def __init__(self, x, y, local_address, remote_address = None):
        self.x = x
        self.y = y
        self.address = local_address
        if remote_address is None:
            self.local = Local(local_address)
        else:
            self.local = Local(local_address, remote_address)        
        self.local.start()

# x, y, local_ip , port for 1x1, port for 20x20, remote_ip_1x1, remote port for 1x1, remote_ip_20x20, remote port for 20x20

if __name__ == "__main__":
  import sys
  x = sys.argv[1]
  y = sys.argv[2]
  local_ip = sys.argv[3]
  if len(sys.argv) == 5:
      taxi = Taxi(x,y,Address(local_ip, sys.argv[4]))
  else:
      remote_ip = sys.argv[5]
      taxi = Taxi(x,y,Address(local_ip, sys.argv[4]),Address(remote_ip, sys.argv[6]))