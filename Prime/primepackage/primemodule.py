#primemodule.py
import random
def isPrime(n):
        """Takes an integer and returns True if it's prime and False if it's not. Will throw a LessThanZeroError if the input is less than zero.
        Example: isPrime(-1) throws a LessThanZeroError, isPrime(3) returns True, and isPrime(1) returns false.""" 
        if n < 0:
                raise LessThanZeroError("The input is less than zero.")
        if n < 2:
            return False
        for i in range (2,n):
            if (n % i) == 0:
                return False
                break
            else:
                return True
            
        
 
def getNPrime(num):
        """Takes an integer, num, and returns a list (of size num) of prime numbers starting from zero."""
        primeList = []
        count = 0
        i = 0
        while count < num:
            if isPrime(i):
                primeList.append(i)
                count += 1
            i += 1
        return primeList        
	
                
            
