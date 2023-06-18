from math import *
from random import *
from matplotlib import pyplot as plt
import numpy as np

          ##################################
          ###                            ###
          #     Useful basic functions     #
          ###                            ###
          ##################################




#max(a,b): ####################
#
#Arguments :
#a -- a real number
#b -- a real number
#
#Return :
#The maximum of (a;b)

def max(a,b):
    if a >= b:
        return a
    else :
        return b

#sig1(x): ####################
#
#Arguments :
#x -- a real number
#
#Return :
#The basic sigmoid function applied to x

def sig1(x):
    return 1/(1+exp(-x))

#sig(x,k): ####################
#
#Arguments :
#x -- a real number
#k -- a strictly positive number
#
#Return :
#The sigmoid function with parameter k applied to x

def sig(x,k):
    return sig1(k*x)

#relu10(x): ####################
#
#Arguments :
#x -- a real number
#
#Return :
#The basic ReLU function applied to x

def relu10(x):
    return max(x,0)

#relu(x): ####################
#
#Arguments :
#x -- a real number
#a -- a real number
#b -- a real number
#
#Return :
#The ReLU function with parameters a and b applied to x

def relu(x,a,b):
    return a*relu10(x-b)
