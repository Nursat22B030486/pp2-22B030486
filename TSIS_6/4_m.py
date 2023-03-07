import time
import math

number = int(input())
time_stop = int(input())/1000
time.sleep(time_stop)
sqrt_num = math.sqrt(number)

print(f'Square root of {number} after {time_stop} miliseconds is {sqrt_num}')
