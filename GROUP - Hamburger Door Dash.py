Group 4
#Hamburger Door Dash




import random


class Order:
   def __init__(self):
       self.burger_count = self.randomBurgers()
      
   def randomBurgers(self):
       return random.randint(1, 20)


class Person:
   def __init__(self):
       self.customer_name = self.randomName()
  
   def randomName(self):
       # List of 9 names for random selection
       asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
       return random.choice(asCustomers)


class Customer(Person):
   def __init__(self):
       super().__init__()
       self.order = Order()


queue= []


dictCustomer = {}


Customer = Customer()
queue.append(customer)


#Update the dictionary with the customer's name and burger count
If customer.customer_name in dictCustomers:
	dictCustomers[customer.customer_name] += customer.order.burger_count
Else: 
	dictCustomers[customer.customer_name] = customer.order.burger_count


#order the dictionary by total number of burgers in descending order
listSortedCustomers = sorted(dictCustomers.items(), key=lambda x: x[1], reverse=True)


#print customer name and the total number of burgers for each customer
For customer in listSortedCustomers:
	print(customer[0],ljust(190,customer[1])
