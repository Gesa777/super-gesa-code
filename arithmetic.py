from math import *
from random import *
from matplotlib import pyplot as plt
import numpy as np

          ############################
          ###                      ###
          #    Basic Arithmetic      #
          ###                      ###
          ############################

#divisors(n): ##########
#
#Arguments :
#n -- a stricly positive integer
#
#Return :
#The list containing the divisors of n

def divisors(n):
    l = []
    for i in range(1,n+1):
        if n % i == 0:
            l.insert(len(l),i)
    return l

#prime(n): ##########
#
#Arguments :
#n -- a stricly positive integer
#
#Return :
#True if n is a prime number and False otherwise

def prime(n):
    if len(divisors(n))==2 :
        return True
    else :
        return False

#printPrimeNumbers(N): ##########
#
#Arguments :
#N -- an integer greater than 2 or equal to 2
#
#Return :
#Empty
#
#Method :
#Print all the prime numbers lower to N

def printPrimeNumbers(N):
    for i in range(2,N+1):
        if prime(i)== True:
            print(i)

#commonDivisors(a,b): ##########
#
#Arguments :
#a -- an integer stricly positive
#b -- an integer stricly positive
#
#Return :
#The list containing the common divisors of a and b

def commonDivisors(a,b):
    return sorted(list( set(divisors(a)) & set(divisors(b))))

#gcd(a,b): ##########
#
#Arguments :
#a -- an integer stricly positive
#b -- an integer stricly positive
#
#Return :
#The greatest common divisor of a and b

def gcd(a,b):
    l = commonDivisors(a,b)
    return l[len(l)-1]
