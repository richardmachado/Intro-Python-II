import sys
from user import User
from product import Product
from department import Department

class Store:
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments

    def __str__(self):
        return("Welcome to the Quarantine Store, don't touch anything")

    def print_departments(self):
        for id, name in self.departments.items():
            print(f"{id}: {name}")
        print()

#user will pas in either a - or 1 command line arugnents
num_args = len(sys.argv)

if num_args == 1:
    user = User(100)
elif num_args == 2:
    user = User(int(sys.argv[1]))
else:
    print("Usage: store.py [money]")
    sys.exit[1]

departments = {
    23: Department(23, "Groceries", [Product("Bananas", 1), Product("Avocados", 2)]),
    1: Department(1, "Toys", [Product("Barbie", 10), Product("Tonka", 12)]),
    12: Department(12, "Books", [Product("Game of Thrones", 10), Product("Working in Public", 25), Product("Twilight", 10)]),
    14: Department(14, "Electronics", [Product("Hitachi 4K TV", 300), Product("Iphone SE", 600)]),
    56: Department(56, "Clothing", [Product("Shirt", 15), Product("Shorts", 12)]),

}

store = Store("Quarantine Store", departments)

while True:
    # print store welcome message
    print(store)
    #print user status
    print(user)

    #print departments
    store.print_departments()

    selection = input("which department would you like to visit? : ")

    if selection == 'quit' or selection == 'q':
        break
    #expect user to type in a number
    dep_num = int(selection)

    if dep_num not in departments:
        print("\n That is not a valid select \n")
        continue

    selected_dep = departments[dep_num]

    # go to that department
    if dep_num in departments:
        #if it is, go to that department
        print(f"\nYou picked department number {dep_num}, the {departments[dep_num].name} department\n")
        #print out all of the products in that department
        selected_dep.print_products()
        #allow user to add a procut to the cart
        product_selection = int(input("What would you like to add to your cart? "))

        possible_products = selected_dep.products
        #Index into the list of products 
        selected_product = possible_products[product_selection]

        user.add_to_cart(selected_product)







