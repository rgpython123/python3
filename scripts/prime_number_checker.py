def isprime(n):
    '''check if integer n is a prime'''

    # make sure n is a positive integer
    n = abs(int(n))

    # 0 and 1 are not primes
    if n < 2:
        return False

    # 2 is the only even prime number
    if n == 2: 
        return True    

    # all other even numbers are not primes
    if not n & 1: 
        return False

    # range starts with 3 and only needs to go up 
    # the square root of n for all odd numbers
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False

    return True


"""
   if not n & 1
NOTE: One number AND another is the bits of one number masked by the bits of another number. If a number AND 1 is 0 (not n & 1 would be True), that means it's divisible by two, since all multiples of 2 have a 0 as the rightmost binary digit.

  11 = 00001011 (Not divisible by 2)      28 = 00011100 (Divisible by 2)
&  1 = 00000001                         &  1 = 00000001
---------------                         ---------------
       00000001                                00000000
"""
