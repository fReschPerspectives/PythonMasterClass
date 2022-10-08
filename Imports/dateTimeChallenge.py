import time
import random

current_year = time.localtime(time.time()).tm_year
current_day = time.localtime(time.time()).tm_mday
current_month = time.localtime(time.time()).tm_mon

print(f"Today is {current_month}-{current_day}-{current_year}.")

input("Press enter to start.")
wait_time = random.randint(1,10)
time.sleep(wait_time)
start_time = time.time()
input("Press enter to stop.")
end_time = time.time()

reaction_time = end_time - start_time

print(f"Your reaction time was: {reaction_time} seconds.")



