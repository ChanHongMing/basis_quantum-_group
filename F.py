class F:
    def __init__(self, sym):
        self.sym = sym
    def __add__(self, other):
        return F(self.x + other.x)
    def __str__(self):
        return str(self.x)
    def __repr__(self):
        return str(self.x)
    def __eq__(self, other):
        return self.x == other.x
    def __hash__(self):
        return hash(self.x)