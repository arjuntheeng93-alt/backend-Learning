#def countdown(n):
 #   while n > 0:
  #      yield n
   #     n -=1
        
        
#for number in countdown(5):
 #   print(number)
 
def read_menu_price(menu): #menu is a list of dictionaries, each dictionary represents a menu item with its name and price. The function iterates through the menu and yields the price of each item one by one.
    for item in menu:#iterates through each item in the menu list
        yield item["Price"]#yields the price of the current menu item, allowing the caller to retrieve it one at a time without loading the entire list of prices into memory at once.
menu = [
    {"Name": "Burger", "Price": 5.99},
    {"Name": "Pizza", "Price": 8.99},
    {"Name": "Salad", "Price": 4.99}]

total =sum(read_menu_price(menu))#calculates the total price of all menu items by summing the prices yielded by the read_menu_price generator function. The sum function takes care of iterating through the generator and adding up the prices until all items have been processed.

print(f"the total price of the menu item is : $(total)")