import sys

x = sys.argv[1]





def primetest(x):
    """ 
    this function checks if the input (have to be int) is prime number or not
    
    execution: from termianl run 
    $ python prime_test.py input
    """

    count = 0
    for i in range(1,x):
        if x%i==0:
            count+=1


    if count == 1:
        p = 'a'
    else:
        p = 'not'

    return p 


print('{} is {} prime number'.format(x, primetest(int(x))))


