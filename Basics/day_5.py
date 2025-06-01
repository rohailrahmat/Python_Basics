chai = " masala tea ", "ginger tea", "ulunge tea"
quantity = 5
order = "i have orderes {quantity} cups of {chai}"
print(order.format(quantity=quantity, chai=chai[1]))  # Using format method to insert values into the string
# f-string for formatting
order = f"i have ordered {quantity} cups of {chai[2]},{chai[0] }and {chai[1]} for my friends"
print(order)  # Using f-string to format the string with variables

program = ["python","javascript","html","css","c++","java"]
print(program.count(program))
print(len(program))

program.append("react js")
print(program)

numbers = [1,2,3,4,5,6,7,8,9,10]
numbers.remove(7)
print(numbers)

numbers.append(11)
print(numbers)
 
numbers.insert(6,7) #in this 6 is the index which we will target put thr number we want to add
print(numbers)

