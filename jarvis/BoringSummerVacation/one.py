import os
import time
input = input('Hoelang moet het aftellen?')



for i in range(int(input)):
    print(int(input)-i)
    time.sleep(1)