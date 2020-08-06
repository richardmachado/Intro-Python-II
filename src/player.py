# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.hp = 100
        self.current_room = current_room
        self.direction = None
        self.game_over = False
        self.items=[]

    def change_room(self, location, move):
        new_direction = move + "_to"
        return getattr(location, new_direction)

    def dropItem(self, item):
        return self.item.remove(item)

    def addItem(self, item):
        return self.items.append(item)
        self.view_items()


    def view_items(self):
        print("Your items: ", [item for item in self.items],' \n')



class Inventory(Player):
    def __init__(self, name, current_room, items=[]):
        super().__init__(name, current_room)
        self.items = items



    def __str__(self):
        return f"{self.items} are in your backpack"