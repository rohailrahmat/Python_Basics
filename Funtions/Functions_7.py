# *kwargs

# in this method we need to give the key and value to run the funtion 
# and we have to use for loop for this  funtion 
# for example 

def sum_of_numbers(**kwargs):
    for key , value in kwargs.items():
        print(f"{key}: {value}")

sum_of_numbers(Name ="rohail", hobby = "coding", languge = "python")
sum_of_numbers(Name ="rhaeel", hobby = "skecting", tools = "pencil")
sum_of_numbers(Name ="romail", hobby = "building", tools = "anything")

