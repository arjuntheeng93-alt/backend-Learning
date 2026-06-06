#def add_to_cart(item, cart=[]):
    #cart.append(item)
    #return cart
    
#solution
def add_to_cart(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart
