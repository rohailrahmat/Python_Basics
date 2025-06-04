# check the uniquness of an item in in a set 
items = ["apples", "orange","graphs","apples","banana","graphs"]

# now we will add an varianle that can store unique items 
unique_items = set() # the set is a funtion that can give a unique output 

# now we will make a loop
for item in items:
    if item in unique_items:
        print("duplicate item is:",item)
        break  #id we remove this it will show all the duplicates
    unique_items.add(item)


 