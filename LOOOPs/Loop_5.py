# another problem
# find the first non repeated numbers that is in the string 

str = "tweeterr"
for char in str:
    print(char)
    if str.count(char) == 1:
        print("the non repeated number is :", char) 
        break


# next example

string ="rohail rahmat baig"

for char in string:
    print(char)
    if string.count(char) == 1:
        print("result is :", char)
        break
                                                                    