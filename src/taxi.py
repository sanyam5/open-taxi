from roamer import Roamer
class Taxi(Roamer):
    def __init__(self, username):
        Roamer.__init__(self, username)
        self.type = "Taxi"
    def set_pricing(self, price_per_km, price_per_minute_wait):
        self.pricing = {
                        "price_per_km":price_per_km, 
                        "price_per_miniute_wait":price_per_minute_wait,
                    }
    def get_pricing(self):
        return self.pricing
    
