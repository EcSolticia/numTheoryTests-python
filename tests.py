
def is_integer(x):
    return (x - int(x)) == 0;

def is_even(x):
    return is_integer(x);
     
def is_odd(x):
    return (not is_even(x));

def is_a_multiple_of(x, y):
    return is_integer(x/y);
    
# brute force method for testing primehood
def brute_is_prime(x):    
    prime = True;
    for i in range(2, x - 1):
        if is_a_multiple_of(x, i):
            prime = False;
            break 
    return prime;
