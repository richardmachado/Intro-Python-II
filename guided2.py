# class Bicycle:
#     def exclaim(self):
#         print("I'm a bicycle")

# class Specialized(Bicycle):
#     def jump(self):
#         print("i'm jumping")

# a_bicycle = Bicycle()
# a_specialized = Specialized()

#Another example --------------------------------------------------------------

# class Student:
#     def __init__(self, name):
#         self.name = name

# class Graduate(Student):
#     def __init__(self, name, graduation_date):
#         super().__init__(name)
#         self.graduation_date = graduation_date


# Composition -----------------------------------

# class Duck:
#     def __init__(self, name, bill_description, tail_length, collar):
#         self.name = name
#         self.bill = Bill(bill_description)
#         self.tail = Tail(tail_length)
#         self.collar = collar

#     def about(self):
#         print(f"this duck has a {self.bill.description} and a {self.tail.length} tail and a {self.collar.color} collar")    

# class Bill:
#     def __init__(self, description):
#         self.description = description

# class Tail:
#     def __init__(self, length):
#         self.length = length

# class Collar:
#     def __init__(self, color):
#         self.color = color

# my_collar= Collar('red')
# duck = Duck("Daffy", "wide orange", "long", my_collar) 
# duck.about()       

people = ["Abe", "Bill", "Charles", "Dolly", "Evelyn", "Frank", "Gunther", "David", "Dolly"]
# comp for names that start with D
a = [person[:3] for person in people if person.startswith('D')]
print(a)

# comp for names that end in Y


# comp for names that start with B through D
# comp for names but in uppercase

c = [person.upper() for person in people ]
print(c)