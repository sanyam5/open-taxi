import network
import topology
from roamer import Roamer

class Customer(Roamer):
    def __init__(self, username):
        Roamer.__init__(self, username)
        self.type = "Customer"
    def search_taxis(self, radius_km=2.0, level=0):
        taxis = network.search(self.loc, level)
        taxis = [taxi for taxi in taxis if (topology.distance_km(taxi.loc, self.loc) < radius_km)] 
        return taxis

