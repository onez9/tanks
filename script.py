



# print('abc\b\bXY\r')
import time
import os

n=30
for i in range(n):
    print('#', end="", flush=True)
    time.sleep(1/60)


for i in range(int(n*5/11)):
    print(' '*(n-1), '#', sep='')
    time.sleep(1/60)
    # os.system('clear')
    
for i in range(n):
    print(f"\r{' '*(n-1-i)}{'#'*(i+1)}", end="", sep="", flush=True)
    time.sleep(1/60)

print()
# print(n*int(5/7))










# print('values values values')