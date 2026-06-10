# i learn about how we can write  comprehensions (in one line)
#get all even nuimber from 1 to 20
#get all words longer than 4 letters from this list:words = ["cat", "python", "dog", "backend", "api", "fastapi"]
# get the price of items that cost menu = [{"name": "pizza", "price":12},{"name": "Beef", "price":13},{"name": "dumpling", "price":10},{"name": "burger", "price":20},

even_number = [num for num in range(1, 21) if num %2 == 0] #this is a list comprehension that generates a list of even numbers from 1 to 20. It iterates through the numbers in the specified range and includes only those that satisfy the condition of being divisible by 2 (i.e., even numbers). The resulting list will contain all even numbers between 1 and 20.

print(even_number)

words = ["cat", "python", "dog", "backend", "api", "fastapi"]
long_words = [word for word in words if len(word) > 4]#this is a list comprehension that creates a new list called long_words. It iterates through each word in the original words list and includes only those words whose length is greater than 4 characters. The resulting long_words list will contain all the words from the original list that have more than 4 letters.
print(long_words)

menus = [{"name": "pizza", "price":12},{"name": "Beef", "price":13},{"name": "dumpling", "price":10},{"name": "burger", "price":20}]

expensive_price = [item["price"] for item in menus if item["price"] > 10]#this is a list comprehension that creates a new list called expensive_price. It iterates through each item in the menus list, which is a list of dictionaries representing menu items with their names and prices. The comprehension checks if the price of each item is greater than 10, and if so, it includes that price in the expensive_price list. The resulting expensive_price list will contain the prices of all menu items that cost more than 10.         
print(expensive_price)




