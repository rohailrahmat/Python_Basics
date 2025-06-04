# check weather the number is prime numberr or not 
# so we know that a number which can divided by itself and the reminder should no be zero called prime number 
# now lets start 
number = 18
Is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % 2) == 0 :
            Is_prime = False
            break

print(Is_prime)

