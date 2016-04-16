from pythonchord.remote import Remote
from pythonchord.chord import Address


def search(id, address):
    rem = Remote(address)
    if id == (rem.find_successor(id).id()):
        return rem
    else:
        return None

# print search(123, Address("127.0.0.1", 45138))
