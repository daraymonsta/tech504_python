print(f"\n{' Task 4 ':=^79}")
# - How are tuples similar to lists? Contain multiple data types
# - Are tuples immutable and what does this mean? Yes, can't be changed after created
# - What other data types are immutable? Numbers, boolean, string
# - What are good use cases for tuples instead of lists? Rerturning from a function? Want the immutability
# - What does the following piece of code do? Counts the number of time "bread" shows in tuple.
essentials = ("bread", "eggs", "milk")
print(essentials)
print(essentials.count("bread"))
# "Stranded on a Desert Island" game
# Rationale: Practice tuples
# Type of exercise: Finish the code
print("You are stranded on a desert island. You can take only THREE items.")
essential_item1 = "t" # input("What is an essential item you would take? ")
essential_item2 = "a" # input("What is an essential item you would take? ")
essential_item3 = "b" # input("What is an essential item you would take? ")
# save the items as a tuple
essentials_tuple = (essential_item1, essential_item2, essential_item3)
# print the tuple
print("Here are your items as a tuple:", essentials_tuple)
print("")
print("I lied. You can take one more item.")
essential_item4 = "s" # input("What is one more essential item you would take? ")
# try to add the 4th item to the tuple
# if you can't add the 4th item, work out how to save the 4th item to the tuple
# YOUR CODE GOES HERE
essentials_tuple = essentials_tuple + (essential_item4,)
print("Here are your items as a tuple (with the 4th item added):", essentials_tuple)