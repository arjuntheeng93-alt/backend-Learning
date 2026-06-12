class MenuItemNotFound(Exception): #parent class for all menu item related exceptions
    pass

class InvalidPrice(Exception):  #parent class for all price related exceptions
    pass

def get_menu_item(menu, item_id): #function to get a menu item by id, raises MenuItemNotFound if item is not found
    for item in menu: #loop through menu items
        if item["id"] == item_id: #if item is found, return it
            return item
        raise MenuItemNotFound(f"Item with id {item_id} does not exist")#if item is not found, raise MenuItemNotFound exception with a message

def create_menu_item(name, price): #function to get a menu id name  and  price, raises invalidprice if price is  negative
    if price < 0:
        raise InvalidPrice(f"Price must be positive, got {price}")
    return {"name": "Pizza", "price" : 12}  #function to create a menu item, returns a dictionary with name and price, raises InvalidPrice if price is negative

menu = [{"id":1, "name" : "Pizza", "price": 12}] #menu is a list of dictionaries, each dictionary represents a menu item with id, name and price
try:
    item = get_menu_item(menu, 99) #try to get a menu item with id 99, which does not exist, should raise MenuItemNotFound exception
except MenuItemNotFound as e:  #catch the MenuItemNotFound exception and print the message
    print(f"Caught: {e}")  #print the message of the exception, which should indicate that the item with id 99 does not exist
    
try:
    item = create_menu_item("Bruger", -5) #try to create a menu item with name "Burger" and price -5, which is invalid, should raise InvalidPrice exception
except InvalidPrice as e:
    print(f"caught: {e}")
    