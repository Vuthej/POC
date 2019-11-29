import datetime # To import datetime module
import winsound # To import winsound module

indicator = ''

#Below code requests for User input.
while indicator != "Q":
    print("\t\tWelcome!!\n\n   Please enter time in 12 hour format\n      Enter 'QUIT' to exit anytime")
    breakfast_time = input("Enter your preferred Breakfast time (HH:MM):")
    #lunch_time = input("Enter your preferred Lunch time (HH:MM):")
    #dinner_time = input("Enter your preferred Dinner time (HH:MM):")
    indicator = input("Press Enter to continue (or) Type Q to exit")

#Below code saves the User data into a text file.
with open("Data1.txt", "a+") as new_file:
    new_file.write(breakfast_time)
    new_file.write("\n")
    #new_file.write(lunch_time)
    #new_file.write("\n")
    #new_file.write(dinner_time)
    #new_file.write("\n")
    
# Code to save current time.
current_time = datetime.datetime.now()

time_data = current_time.strftime("%I:%M")

# Below code will compare user entered time with current time and will check whether or not to send a reminder.
with open("Data1.txt") as input_file:
    for line in input_file:
        if int(line[:2]) == int(time_data[:2]):
            if int(line[3:]) == int(time_data[3:]):
                frequency = 300
                duration = 1000
                winsound.Beep(frequency, duration)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
initial code
# Type code here
# Type code for classes here

class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_description = "none"
        self.item_price = 0
        self.item_quantity = 0
    
    def print_item_cost(self):
        return ("%s %d @ $%d = $%d" % (self.item_name, self.item_quantity, self.item_price, self.item_price * self.item_quantity))
    
    def __add__(self, other):
        print(self.item_price)
        print(self.item_quantity)
        print(other.item_price)
        print(other.item_quantity)
        total = (self.item_price * self.item_quantity) + (other.item_price * other.item_quantity)
        return total
    
    def print_item_description(self):
        return ("Bottled Water: Deer Park, 12 oz.")

class ShoppingCart:
    def __init__(self, customer_name, current_date):
        self.customer_name = "none"
        self.current_date = "January 1, 2016"
    
    cart_items = []
    
    def add_item(self, ItemToPurchase):
        #cart_items.append(ItemToPurchase())
        cart_items.append(ItemToPurchase)
    
    def remove_item(self, item_name):
        if self.item_name in cart_items:
            cart_items.remove(item_name)
        else:
            print("Item not found in cart. Nothing removed.")
    
    def modify_item(self, ItemToPurchase):
        if ItemToPurchase.self.customer_name in cart_items:
            print("test")
            #Fixme
    
    def get_num_items_in_cart(self):
        return len(cart_items)
            
    def get_cost_of_cart(self):
        final_cost = 0
        #for item in cart_items:
            #cost of item * number of items
            #fixme
    
    def print_total(self):
        if len(cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print("SHOPPING CART IS NOT EMPTY")
    
    def print_descriptions(self):
        print("For each item, call print_item_description")
        
        

if __name__ == "__main__":
    new_total = []
    for loop in range(2):
        #print("Item %d" % (loop + 1))
        #if loop == 0:
        item1 = ItemToPurchase()
        item1.item_name = input("Enter the item name:\n")
        item1.item_price = float(input("Enter the item price:\n"))
        item1.item_quantity = int(input("Enter the item quantity:\n"))
        #elif loop == 1:
        #    item2 = ItemToPurchase()
        #    item2.item_name = input("Enter the item name:\n")
        #    item2.item_price = float(input("Enter the item price:\n"))
        #    item2.item_quantity = int(input("Enter the item quantity:\n"))
        print()
           #print("TOTAL COST")
        new_total.append(item1.item_price * item1.item_quantity)
        print(item1.print_item_cost())
            #print(item2.print_item_cost())
        print()
    #print("Total: $%d" % (item1 + item2))
    print("Total: $%d" % (sum(new_total)))
    john_doe = ShoppingCart('John Doe', 'February 1, 2016')
    # Type main section of code here

                
                