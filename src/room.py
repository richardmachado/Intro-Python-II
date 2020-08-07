# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, item=None):
        self.name = name
        self.description = description
        self.item = item
        self.visited = False
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def addItem(self, item):
        self.item=item

    def __str__(self):
        return f"{self.name}. {self.description}"




