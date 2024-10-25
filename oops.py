#self- self is a variable which refers to current class instance/objects. self ek tarah ka default variable hota hai jo ki object ke memory address ko point krta hai. is variable ka use class ke sabhi variables aur methods ko refer krne ka kaam karta hai
#jab bhi hum object banate hai kisi class ka to jo object_name hota hai wo object ka memory location contain krta hai. aur ye jo self hota hai wo us memory location ke address ko point krta hai internally. taki hum us class ke sare variables aur methods ko call kr sake self ki madad se


# object= hum jitni bar kisi class ke objects ko banate hai utni hi baar us class se related objects create hote hai



# __init__() method - this method is used to initialize the variables while making the objects. means jaise hi class create krenge ye variables update ho jayenge



#EXAMPLE-1 take a number from the user and make a method which tells me whether the number is palindrome or not using the ispalindrome(number) using class

class Number:
    def __init__(self, number): 
        self.number = number

    def ispalindrome(self):
        return str(self.number) == str(self.number)[::-1]

num1 = Number(5)
print(num1.ispalindrome())

num2 = Number(121)
print(num2.ispalindrome())

num3 = Number(123)
print(num3.ispalindrome())


#Example-2 Reactangle-  Write a Python class named Rectangle constructed from length and width and a method that will compute the area of a rectangle.
#EX-1
class Rectangle:
    def __init__(self,l,w):
        self.l=l;
        self.w=w;
    
    def Area(self):
        return self.l* self.w
        

x= Rectangle(10,20);
print(x.Area())

#EX-2 in this i will not initialize the constructor at time of creating the object. in the area calculator i will pass the data in the parameter
class Rectangle:
    def __init__(self):
        """Initialize the Rectangle without parameters."""
        pass

    def Area(self, l, w):
        """Calculate the area of the rectangle with given length l and width w."""
        return l * w

x = Rectangle()
result = x.Area(10, 20)
print(result)

#EXAMPLE-3 Write a Python class named Circle constructed from a radius and two methods that will compute the area and the perimeter of a circle.
class Circle:
    def __init__(self,r):
        self.r=r
    
    def Perimeter(self):
        return 2*3.14*self.r
        
    def Area(self):
        return 3.14*self.r*self.r
        
x=Circle(7);
print(x.Area())
print(x.Perimeter())

#EXAMPLE-4 Write a Python class named Number and make the sum of the two number. and the value will not be passed while making the objects
class Number:
    def __init__(self):
        self.a=5;
        self.b=9;
        
    def sum(self):
        return self.a+self.b;
        
x = Number();
print(x.sum())

#EXAMPLE-5 Write a Python class named Number and make the sum of the two number. and the value will be passed while making the objects
class Number:
    def __init__(self,a,b):
        self.a=a;
        self.b=b;
        
    def sum(self):
        return self.a+self.b;
        
x = Number(6,11);
print(x.sum())

#EXAMPLE-6 reverse the string class
class Reverse:
    def __init__(self,input):
        self.input=input;
    
    def reverse(self):
        return self.input[::-1]
        
x=Reverse("Hello World");
print(x.reverse())

#EXAMPLE-5 check the string is palindrome or not
class Reverse:
    def __init__(self,input):
        self.input=input;
    
    def reverse(self):
        return self.input[::-1]
        
    def ispalindrome(self):
        return self.input==self.input[::-1]
        
x=Reverse("Hello World");
print(x.reverse())
print(x.ispalindrome())

#EXAMPLE-6 Write a Python class that has two methods: get_String and print_String , get_String accept a string from the user and print_String prints the string in upper case

class String:
    def __init__(self,input):
        self.input=input;          # self.input ko hum kuch bhi likh svariable hai aur is variable me hum parameter ki value ko assign kar rhe hai
        
    def reverse(self):
        return self.input[::-1]
        
    def ispalindrome(self):
        return self.input==self.input[::-1]
        
    def Uppercase(self):
        return self.input.upper()  
        
x = String("hello world");
print(x.reverse())
print(x.ispalindrome())
print(x.Uppercase())

#EXAMPLE- . Write a Python class BankAccount with attributes like account_number, balance, date_of_opening and customer_name, and methods like deposit, withdraw, and check_balance.
class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening, balance=0):
        """Initialize the bank account with account number, customer name, date of opening, and optional balance."""
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} successfully. New balance: {self.balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount} successfully. New balance: {self.balance}")
            else:
                print("Insufficient balance!")
        else:
            print("Invalid withdrawal amount!")

    def check_balance(self):
        """Check the current balance of the account."""
        print(f"Current balance: {self.balance}")

# Example usage:
account = BankAccount("123456789", "John Doe", "2024-01-01", 1000)
account.check_balance()
account.deposit(500)
account.withdraw(300)
account.withdraw(2000)

#EXAMPLE Write a Python class Inventory with attributes like item_id, item_name, stock_count, and price, and methods like add_item, update_item, and check_item_details.
#Use a dictionary to store the item details, where the key is the item_id and the value is a dictionary containing the item_name, stock_count, and price.

class Inventory:
    def __init__(self):
        """Initialize the inventory with an empty dictionary to store items."""
        self.items = {}

    def add_item(self, item_id, item_name, stock_count, price):
        """Add a new item to the inventory."""
        if item_id not in self.items:
            self.items[item_id] = {
                'item_name': item_name,
                'stock_count': stock_count,
                'price': price
            }
            print(f"Item '{item_name}' added successfully.")
        else:
            print(f"Item with ID '{item_id}' already exists in the inventory.")

    def update_item(self, item_id, stock_count=None, price=None):
        """Update the stock count or price of an existing item."""
        if item_id in self.items:
            if stock_count is not None:
                self.items[item_id]['stock_count'] = stock_count
            if price is not None:
                self.items[item_id]['price'] = price
            print(f"Item with ID '{item_id}' updated successfully.")
        else:
            print(f"Item with ID '{item_id}' does not exist.")

    def check_item_details(self, item_id):
        """Check the details of an item by its ID."""
        if item_id in self.items:
            item = self.items[item_id]
            print(f"Item ID: {item_id}")
            print(f"Item Name: {item['item_name']}")
            print(f"Stock Count: {item['stock_count']}")
            print(f"Price: {item['price']}")
        else:
            print(f"Item with ID '{item_id}' does not exist in the inventory.")

# Example usage:
inventory = Inventory()
inventory.add_item(101, "Laptop", 50, 999.99)
inventory.add_item(102, "Smartphone", 100, 599.99)
inventory.check_item_details(101)
inventory.update_item(102, stock_count=90, price=579.99)
inventory.check_item_details(102)
inventory.add_item(101, "Laptop", 50, 999.99)

#Write a Python class Restaurant with attributes like menu_items, book_table, and customer_orders, and methods like add_item_to_menu, book_tables, and customer_order.
#Perform the following tasks now:

#Now add items to the menu.
#Make table reservations.
#Take customer orders.
#Print the menu.
#Print table reservations.
#Print customer orders.
#Note: Use dictionaries and lists to store the data.

class Restaurant:
    def __init__(self):
        """Initialize the restaurant with empty menu, table bookings, and customer orders."""
        self.menu_items = {}  # Store menu items with item name as key and price as value
        self.booked_tables = []  # List to store booked table numbers
        self.customer_orders = {}  # Dictionary to store customer orders with table number as key

    def add_item_to_menu(self, item_name, price):
        """Add a new item to the menu."""
        if item_name not in self.menu_items:
            self.menu_items[item_name] = price
            print(f"Item '{item_name}' added to the menu at ${price}.")
        else:
            print(f"Item '{item_name}' already exists in the menu.")

    def book_table(self, table_number):
        """Book a table for the customer."""
        if table_number not in self.booked_tables:
            self.booked_tables.append(table_number)
            print(f"Table {table_number} has been booked successfully.")
        else:
            print(f"Table {table_number} is already booked.")

    def customer_order(self, table_number, order_items):
        """Take customer order and associate it with a table number."""
        if table_number in self.booked_tables:
            if table_number not in self.customer_orders:
                self.customer_orders[table_number] = []
            self.customer_orders[table_number].extend(order_items)
            print(f"Order taken for table {table_number}: {order_items}")
        else:
            print(f"Table {table_number} is not booked yet. Please book the table first.")

    def print_menu(self):
        """Print the current menu."""
        if self.menu_items:
            print("Menu Items:")
            for item, price in self.menu_items.items():
                print(f"{item}: ${price}")
        else:
            print("The menu is empty.")

    def print_table_reservations(self):
        """Print all booked tables."""
        if self.booked_tables:
            print("Booked Tables:", self.booked_tables)
        else:
            print("No tables have been booked.")

    def print_customer_orders(self):
        """Print all customer orders."""
        if self.customer_orders:
            print("Customer Orders:")
            for table, orders in self.customer_orders.items():
                print(f"Table {table}: {orders}")
        else:
            print("No orders have been placed.")

# Example usage:
restaurant = Restaurant()
restaurant.add_item_to_menu("Pasta", 12.99)
restaurant.add_item_to_menu("Burger", 9.99)
restaurant.add_item_to_menu("Pizza", 14.99)
restaurant.book_table(1)
restaurant.book_table(2)
restaurant.customer_order(1, ["Pasta", "Burger"])
restaurant.customer_order(2, ["Pizza"])
restaurant.print_menu()
restaurant.print_table_reservations()
restaurant.print_customer_orders()
