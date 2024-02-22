list = ["crocodile", "monkey", "lion", "zebra"]
list.remove("monkey")
list.append("cheatah")
list.remove("cheatah")
print(list)


groceries = ["apples", "milk", "cheese", "bread"]
groceries. append("coffee") 	# ["apples", "milk", "cheese", "bread", "coffee"]
groceries.insert(0, "carrots") # ["carrots","apples", "milk", "cheese", "bread", "coffee"]
groceries.insert(1, "peas") # ["carrots","peas","apples", "milk", "cheese", "bread", "coffee"]
groceries.pop() # ["carrots", "peas", "apples", "milk", "cheese", "bread"]
groceries.pop(0) # ["peas","apples", "milk", "cheese", "bread"]
groceries.remove("cheese") # ["peas","apples", "milk", "bread"]