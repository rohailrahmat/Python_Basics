numbers = [1,-2, 3,-4, 5, -6, -7, 8,-9, 10,99]
positive_int_count = 0
for num in numbers:
    if num > 0:
        positive_int_count = positive_int_count + 1
print("the positive integer count is",positive_int_count)
