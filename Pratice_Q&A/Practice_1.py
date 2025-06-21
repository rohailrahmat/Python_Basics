# 🔁 Loops Practice
# 1. 🔢 Print Numbers with for loop
# Write a program that prints numbers from 1 to 10 using a for loop.
# x = 0
# for i in range(1,11):
#     print(i)
    



# 2. 🔁 while loop: Count Down
# Write a program that counts down from 5 to 1 using a while loop, and then prints "Blast off!".
# count = 5
# while count > 0:
#     print(count)
#     count -= 1

# print("Blast off!")


# 3. 🔁 for loop with condition
# Print all even numbers between 1 and 20 using a for loop and if.
# for num in range(1 , 21):
#     if num % 2 == 0:
#         print(num)


# 4. 🔁 Sum of Numbers
# Use a for loop to calculate the sum of numbers from 1 to 100.
# total = 0
# for i in range(1 , 101):
#     total += i
# print(total)


# 5. 🧮 Multiplication Table
# Ask the user for a number and print its multiplication table (1 to 10).
# num = int(input("please enter a number:"))
# for i in range(1 ,11):
#     print(f"{num} X {i} = {num * i}")

# 🧰 Functions Practice
# 6. 🔧 Function to Greet
# Write a function greet(name) that prints Hello, name!.
# def greet (name):
#     print("Hello",name)
# greet("rohail")


# 7. ➕ Function to Add Two Numbers
# Write a function add(a, b) that returns the sum of two numbers.
# def add(a , b):
#     return a + b
# result = add(1,4)
# print("this is the addition:", result)

# 8. 📦 Factorial Function (using loop)
# Write a function factorial(n) that returns the factorial of a number using a loop.
# def fatorial_function(n):
#     result = 1
#     for i in range(1 ,n + 1):
#         result *= i
#     return result
# print("Factorial is ",fatorial_function(10))

# 9. 🔁 Check Prime Number
# Write a function is_prime(n) that checks whether a number is prime or not.

# def is_prime(n):
#     if n <= 1:
#         return False  # 0 and 1 are not prime

#     for i in range(2, int(n ** 0.5) + 1):  # only go up to sqrt(n)
#         if n % i == 0:
#             return False  # divisible by something, so not prime

#     return True  # it's prime if loop completes

# print(is_prime(7))   
# print(is_prime(10))  
# print(is_prime(2))   
# print(is_prime(1))   


# 10. 📦 Combine Loops and Functions
# Create a function print_even_in_range(start, end) that uses a loop to print all even numbers between two given numbers.def print_even_in_range(start, end):
def print_even_in_range(start, end):
        for num in range(start ,end + 1):
             if num % 2 == 0:
                print(num)
print_even_in_range(10, 20)
