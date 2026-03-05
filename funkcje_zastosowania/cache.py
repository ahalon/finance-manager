from time import sleep
from time import time
import functools


@functools.lru_cache()
def Factorial(n):

    sleep(0.1)
    if n == 1:
        return 1
    else:
        return n * Factorial(n - 1)
    
start = time()    
for i in range (1, 11):
    print(f"{i}! = {Factorial(i)}")
stop = time()
print(f"Obliczenia zajęły {stop - start} sekund")

print(Factorial.cache_info())


# LAB
from time import time, sleep
import functools

@functools.lru_cache()
def fib(n):
    sleep(0.1) # Symulacja ciężkiej roboty
    if n < 2:
        result = n
    else:
        result = fib(n-1) + fib(n-2)
        
    return result

start = time()
for i in range(1, 11):
    print(f"fib({i}) = {fib(i)}")
stop = time()
print(f"Obliczenia zajęły {stop - start} sekund")
print(fib.cache_info())