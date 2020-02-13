import sys

x = sys.argv[1]

def primetest(x):
    """ 
    this function checks if the input (have to be int) is prime number or not
    
    execution: from termianl run 
    $ python prime_test.py input
    """
    for i in range(2,x):
        if x%i==0:
            print(x,' is not a prime number')
            break
    else:
        print(x, ' is a prime number')

if __name__ == "__main__":
    primetest(int(x))
