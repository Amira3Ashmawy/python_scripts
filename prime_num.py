import random 
import numpy as np
import math
def is_prime(num):
    num_sqrt = int(math.sqrt(num))+1
    for i in range(2,num_sqrt):
        if not (num % i): 
            return False
    return True
def get_prime_nums():
    prime_arr =np.empty((1000),int)
    indx = 0 
    i = 0
    while indx < 1000:
        if is_prime(i):
            prime_arr[indx] = i 
            indx+= 1
        i+=1
    prime_arr = np.reshape(prime_arr,(10,10,10),order='F')
    return prime_arr
print(get_prime_nums())
