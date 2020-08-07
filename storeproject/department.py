class Department:
    def __init__(self, id, name, products=[]):
        self.id = id
        self.name = name
        self.products = products


    def __str__(self):
        return f"Department {self.id}, {self.name}"

    def print_products(self):
        for id, p in enumerate(self.products):
            print(f"{id}: {p}")
        print()