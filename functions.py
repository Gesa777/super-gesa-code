from math import *
from random import *
from matplotlib import pyplot as plt
import numpy as np

          ##################################
          ###                            ###
          #     Useful basic functions     #
          ###                            ###
          ##################################

########## max ##########
# Arguments : a, b two real numbers
# Return : the maximum of (a;b)
def max(a,b):
    if a >= b:
        return a
    else :
        return b

########## sig1 ##########
# Arguments : x a real number
# Return : the basic sigmoid function applied to x
def sig1(x):
    return 1/(1+exp(-x))

########## sig ##########
# Arguments : x a real number and k a strictly positive number
# Return : the sigmoid function with parameter k applied to x
def sig(x,k):
    return sig1(k*x)

########## relu10 ##########
# Arguments : x a real number
# Return : the basic ReLU function applied to x
def relu10(x):
    return max(x,0)

########## relu ##########
# Arguments : x, a, b three real numbers
# Return : the ReLU function with parameters (a;b) applied to x
def relu(x,a,b):
    return a*relu10(x-b)
