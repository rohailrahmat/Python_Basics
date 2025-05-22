# conditional statements
total_bill = 990 
discount = 10 
if total_bill > 100:
    print("the bill is greater then your got a discount of 10%")
    total_bill = total_bill - (total_bill * discount / 100)
    print(total_bill)

else: 
    print("the bill is less then 100 no discout")
    print("your total bill is:", total_bill)
# https://github.com/rohailrahmat/Python_Basics.git