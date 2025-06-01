number = 5 

for i in range(1 , 11): #this is the range on which the loop will end  just like start from 1 and stop at 10 
    if i == 7:
        continue
    print(number, "x", i, "=",number* i)


# out put
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50

number_2 = 10

for i in range(1, 21):
    if i == 7:
        continue #this is a key word which is used to skip the specific number from the loop 
    print(number, "X" ,i, "=", number_2 * i)

    # output
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25 here the 7 is skiped and move to 8 by the continue the counting
# 5 x 6 = 30
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50
# 5 X 1 = 10
# 5 X 2 = 20