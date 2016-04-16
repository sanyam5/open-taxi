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
    def __init__(self, x, y, local_address_1x1, local_address_20x20, remote_address_1x1 = None, remote_address_20x20 = None):
        self.x = x
        self.y = y
        self.address_1x1 = local_address_1x1
        self.address_20x20 = local_address_20x20
        if remote_address_1x1 is None:
            self.local_1x1 = Local(local_address_1x1,setid=generate_id(x,y,1))
        if remote_address_20x20 is None:
            self.local_20x20 = Local(local_address_20x20,setid=generate_id(x,y,20))
        if remote_address_1x1:
            self.local_1x1 = Local(local_address_1x1, remote_address_1x1,setid=generate_id(x,y,1))
        if remote_address_20x20:
            self.local_20x20 = Local(local_address_20x20, remote_address_20x20,setid=generate_id(x,y,1))        
        self.local_1x1.start()
        self.local_20x20.start()

# x, y, local_ip , port for 1x1, port for 20x20, remote_ip_1x1, remote port for 1x1, remote_ip_20x20, remote port for 20x20

if __name__ == "__main__":
  import sys
  x = sys.argv[1]
  y = sys.argv[2]
  local_ip = sys.argv[3]
  if len(sys.argv) == 6:
      taxi = Taxi(x,y,Address(local_ip, sys.argv[4]),Address(local_ip, sys.argv[5]))
  else:
      remote_ip_1x1 = sys.argv[6]
      remote_ip_20x20 = sys.argv[8]
      taxi = Taxi(x,y,Address(local_ip, sys.argv[4]),Address(local_ip, sys.argv[5]),Address(remote_ip_1x1, sys.argv[7]),Address(remote_ip_20x20, sys.argv[9]))