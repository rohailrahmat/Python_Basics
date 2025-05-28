# movie ticket pricing 
# now
age = 12
day = "sunday"
price = 12 

# now this program have 2 way to slove 
# 1
if age <= 18:
    print("you are an child your tiket price is $", price -2)
elif age > 18:
    print("you are a adult your tiket price is $", price)
else:
    print("you are a senior citizen your tiket price is $", price - 5)

if day == "sunday":
    print("you get a discount of 5$ Because it is sunday")
    price = price - 2
    print("you ticket price is",price)
# now this program have a short syntax code to perform the same thing 

# eg.2
age_2 = 16
day_2 = "friday"

price_2 = 10  if age_2 <= 18 else 8
print(price_2)
if day_2 == "friday":
    print("enjoy your discount", price_2 - 2 )
else:
    print("you tikcet price:",price_2)