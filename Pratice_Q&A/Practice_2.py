# lets go 
#1
# FizzBuzz Problem

# for i in range(1 ,50):
#     if i % 3 == 0:
#         print("fizz",i)
#     elif i % 5 == 0:
#         print("buzz",i)
#     else:
#         print("both", i)
    

#2
# Reverse a Number

# Write a function reverse_number(n) that reverses an integer.
# Example: 1234 → 4321

def reverse_number(n):
    reverse_number = int(str(n)[::-1])
    return reverse_number

print("Reversed",reverse_number(1234))










# ✨ Check Palindrome

# Write a function is_palindrome(s) that checks if a string is a palindrome (same forward and backward)
# Example: madam → True

# 🔢 Count Digits in a Number

# Write a function that counts how many digits a number has.
# Example: count_digits(12345) → 5

# 🎲 Guess the Number Game (Mini Project!)

# Build a small game:

# Computer picks a random number 1 to 20

# User guesses until correct

# Show attempts at the end

# 🛠️ BONUS: Stretch Questions (if you want more)
# 🔠 Uppercase Converter

# Write a function to_uppercase(s) without using .upper()

# 🎴 Sum of Digits

# Write a function sum_digits(n)
# Example: 123 → 1 + 2 + 3 = 6