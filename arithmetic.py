from math import *
from random import *
from matplotlib import pyplot as plt
import numpy as np

          ############################
          ###                      ###
          #    Basic Arithmetic      #
          ###                      ###
          ############################


def divisors(n):
"""
Arguments : n a strictly positive integer
Return : the list containing the divisors of n
"""
    l = []
    for i in range(1,n+1):
        if n % i == 0:
            l.insert(len(l),i)
    return l


def prime(n):
"""
Arguments : n a strictly positive integer
Return : True if n is a prime number and False otherwise
"""
    if len(divisors(n))==2 :
        return True
    else :
        return False


def printPrimeNumbers(N):
"""
Arguments : N an integer greater or equal to 2
Return : empty
Process : print all the prime numbers lower to N
"""
    for i in range(2,N+1):
        if prime(i)== True:
            print(i)


def commonDivisors(a,b):
"""
Arguments : a, b two strictly positive integer
Return : the list containing the common divisors of a and b
"""
    return sorted(list( set(divisors(a)) & set(divisors(b))))


def gcd(a,b):
"""
Arguments : a, b two strictly positive integer
Return : the greatest common divisor of a and b
"""
    l = commonDivisors(a,b)
    return l[len(l)-1]
