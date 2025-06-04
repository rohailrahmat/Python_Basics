# now in this code we will play with some time 
# firstly we will import time for the operation
import time

wait_time = 1
max_retries = 4
attempts = 0

while attempts < max_retries:
    print("attempts",attempts +1 ,"wait time is :",wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1