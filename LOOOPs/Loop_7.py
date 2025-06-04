# let take a input from user and ask for write number between 1 and 10 

while True:
    number = int(input("enter the number btw 1 and 10:"))
    if 1 >= number <= 10:
        print("thank you for the response")
        break
    else:
        print("please try again!!!")
    