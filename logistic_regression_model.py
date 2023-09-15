from math import *
from random import *
from matplotlib import pyplot as plt
import numpy as np

################################################################################
###                                                                          ###
#                                                                              #
#                     Integration of a multidimensional                        #
#                        logistic regression model                             #
#                                                                              #
###                                                                          ###
################################################################################

################################################################################


########## sigmoid_function ##########
# Argument : X is a float or a matrix
# Return : the value of the sigmoid function applied to X i.e. 1/(1+exp(-X))
# Process : no
def sigmoid_function(X):
    return 1/(1+np.exp(-X))


########## initialize_with_zeros ##########
# Argument : dim is the number of variables
# Return : a tuple with the vector W initialized to zero and the float b equal to zero
# Process : no
def initialize_with_zeros(dim):
    b = 0
    W = np.zeros((dim,1))
    return (W,b)


########## propagate ##########
# Argument 1 : W is the interceptor parameter vector
# Argument 2 : b is the interceptor parameter scalar
# Argument 3 : Xi is the data matrix associated with the program input variables
# Argument 4 : Y is the data row vector associated with the program output variable
# Return : a tuple with the value of the cost function and the values of its partial derivatives (relative to W and b)
# Process : no
def propagate(W,b,Xi,Y):
    m = Y.shape[1]
    Z = np.dot(W.T,Xi)+b
    A = sigmoid_function(Z)
    dJdZ = A - Y
    dJdW = np.dot(Xi,dJdZ.T)/m
    dJdb = np.sum(dJdZ)/m
    J = -(np.dot(Y,np.log(A).T)+ np.dot(1-Y,np.log(1-A).T))/m
    return (J,dJdW,dJdb)


########## optimize ##########
# Argument 1 : W is the interceptor parameter vector
# Argument 2 : b is the interceptor parameter scalar
# Argument 3 : Xi is the data matrix associated with the program input variables
# Argument 4 : Y is the data row vector associated with the program output variable
# Argument 5 : N_iter is number of iterations in the dradient descent implementation
# Argument 6 : alpha is the learning rate
# Argument 7 : True or False to plot the cost function during the gradient descent
# Argument 8 : delta_iter is the step used to plot the cost function if argument 7 is True
# Return : a tuple with the vector W and the float b optimized by gradient descent
# Process : if argument 7 is True the program save the graph of the cost function evolution
def optimize(W,b,Xi,Y,N_iter,alpha, plotting = True, delta_iter = 100):

    if plotting :
        x = np.linspace(0,N_iter-delta_iter,N_iter//delta_iter)
        y = np.linspace(0,N_iter-delta_iter,N_iter//delta_iter)

    for k in range(0,N_iter):

        if plotting and k % delta_iter ==0:
            y[k//delta_iter] = propagate(W,b,Xi,Y)[0]

        W = W - alpha*propagate(W,b,Xi,Y)[1]
        b = b - alpha*propagate(W,b,Xi,Y)[2]
    if plotting :
        plt.clf()
        plt.title("Minimization of the cost function")
        plt.xlabel("Number of steps in gradient descent")
        plt.ylabel("Cost value")
        plt.grid(True)
        plt.plot(x,y,"r-", linewidth=0.85)
        plt.savefig("minimization_cost_graph.png")

    return (W,b)


########## predict ##########
# Argument 1 : W is the interceptor parameter vector
# Argument 2 : b is the interceptor parameter scalar
# Argument 3 : Xi is the data matrix associated with the program input variables
# Return : a tuple with two vectors : the vector of probabilities that the outputs variables equal to one and a binary vector (1 if probability is greater than 0.5 and 0 otherwise)
# Process : no
def predict(W,b,Xi):
    res = sigmoid_function(np.dot(Xi.T,W)+b)
    m = Xi.shape[1]
    binary_res = np.zeros((m,1))
    for i in range(0,m):
        if res[i]>0.5:
            binary_res[i][0] = 1
    return (res,binary_res)


########## model ##########
# Argument 1 : Xi_train is the training data matrix associated with the program input variables
# Argument 2 : Y_train is the training data row vector associated with the program output variable
# Argument 3 : Xi_dev is the test data matrix associated with the program input variables
# Argument 4 : Y_dev is the test data row vector associated with the program output variable
# Argument 5 : N_iter is number of iterations in the dradient descent implementation
# Argument 6 : alpha is the learning rate
# Argument 7 : True or False to plot the cost function during the gradient descent
# Argument 8 : delta_iter is the step used to plot the cost function if argument 7 is True
# Return : a tuple with two numbers : the prediction error on the training set and the prediction error on the dev set
# Process : if argument 7 is True the program save the graph of the cost function evolution
def model(Xi_train, Y_train, Xi_dev, Y_dev, N_iter, alpha,plotting_cost = True, delta_iter = 100):
    n_train = Xi_train.shape[0]
    m_train = Xi_train.shape[1]
    m_dev = Xi_dev.shape[1]

    (W,b) = initialize_with_zeros(n_train)

    (W,b) = optimize(W,b,Xi_train,Y_train,N_iter,alpha,plotting_cost,delta_iter)

    result_train = predict(W,b,Xi_train)[1]

    result_dev = predict(W,b,Xi_dev)[1]

    error_train = 0
    for j in range(0,m_train):
        if result_train[j][0] != Y_train[0][j]:
            error_train = error_train + 1

    error_dev = 0
    for j in range(0,m_dev):
        if result_dev[j][0] != Y_dev[0][j]:
            error_dev = error_dev + 1

    return (error_train/m_train, error_dev/m_dev)
