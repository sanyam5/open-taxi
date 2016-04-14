class Roamer:
    def __init__(self, username):
        self.username = username
        self.loc = None
    def get_loc(self):
        return self.loc
    def set_loc(self, loc):
        self.loc = loc

