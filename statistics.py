from math import *
from random import *
from matplotlib import pyplot as plt
import numpy as np


          ################################
          ###                          ###
          #  Basic univariate statistics #
          ###                          ###
          ################################

class Series:
    #Constructor : list represents the one dimensional series
    def __init__(self, list, nX):
        #Series
        self.series = list
        #Size (total effective)
        self.size = len(list)
        #Sum of the elements
        self.sum = sum(list)
        #Mean
        self.mean = self.sum/self.size
        #Squared elements sum
        self.sumSquares = sum(np.square(list))
        #Variance
        self.var = self.sumSquares/self.size - self.mean**2
        #Standard deviation
        self.stdDev = sqrt(self.var)
        #Ordered series
        self.orderSeries = sorted(list)
        #Minimum
        self.min = self.orderSeries[0]
        #Maximum
        self.max = self.orderSeries[self.size-1]
        #Scope
        self.scope = self.max - self.min
        #Median
        if self.size % 2 == 1:
            self.med = self.orderSeries[(self.size-1)//2]
        else :
            self.med = (self.orderSeries[self.size//2 - 1] +  self.orderSeries[self.size//2])/2.
        #First quartile
        if self.size/4 == int(self.size/4):
            self.quartile1 = self.orderSeries[self.size//4 - 1]
        else :
            self.quartile1 = self.orderSeries[self.size//4]
        #Third quartile
        if 3*self.size/4 == int(3*self.size/4):
            self.quartile3 = self.orderSeries[3*self.size//4 - 1]
        else :
            self.quartile3 = self.orderSeries[3*self.size//4]
        #Interquartile gap
        self.deltaQ = self.quartile3 - self.quartile1
        #Number of distinct values
        counter = 1
        for i in range(0,self.size-1):
            if self.orderSeries[i]< self.orderSeries[i+1]:
                counter = counter + 1
        self.nbrDistinct = counter
        #Variable name
        self.name = nX

"""
save
Arguments : fileName is the backup file nam
Return : empty
Process : save the quantitative indicators about the series in the file
"""
    def save(self, fileName):
        file = open(fileName, "a")
        file.write("Univariate statistical study :")
        file.write('\n')
        file.write("\n" + self.name)
        file.write('\n')
        file.write("\nData number N = " + str(self.size))
        file.write("\nData sum S = " + str(self.sum))
        file.write("\nData squared sum S2 = " + str(self.sumSquares))
        file.write("\nNumber of distinct values p = " + str(self.nbrDistinct))
        file.write("\nMean mu = " + str(self.mean))
        file.write("\nVariance Var = " + str(self.var))
        file.write("\nStandard deviation sigma = " + str(self.stdDev))
        file.write("\nMinimum min = " + str(self.min))
        file.write("\nMaximum max = " + str(self.max))
        file.write("\nScope e = " + str(self.scope))
        file.write("\nMedian M = " + str(self.med))
        file.write("\nFirst quartile Q1 = " + str(self.quartile1))
        file.write("\nThird quartile Q3 = " + str(self.quartile3))
        file.write("\nInterquartile gap DeltaQ = " + str(self.deltaQ))
        file.close()

"""
histogram
Arguments : nbrClasses is the classes number for the histogram, title is the graph title and fName is the backup file name
Return : empty
Process : Print and save the histogram of the distribution
"""
    def histogram(self, nbrClasses, title,fName):
        x = self.series
        plt.title(title)
        plt.xlabel(self.name)
        plt.ylabel("Effective distribution")
        plt.grid(alpha =.6, linestyle =':')
        plt.hist(x, bins = nbrClasses, color = 'blue', edgecolor="yellow" )
        plt.savefig(fName)
        plt.show()

"""
box
Arguments : title is the graph title and fName is the backup file name
Return : empty
Process : print and save the box diagramm of the distribution
"""
    def box(self,title, fName):
        x=self.series
        plt.boxplot(x,vert = 0, medianprops = {"color": "red", "linewidth" : 2.5},
        boxprops = {"linewidth" : 1.5}, whiskerprops={"color": "black", "linewidth": 1.5},
        capprops={"color": "black", "linewidth": 1.5})
        plt.title(title)
        plt.xlabel(self.name)
        plt.grid(alpha =0.5, linestyle =':')
        ax = plt.gca()
        ax.spines['top'].set_color('none')
        ax.spines['left'].set_color('none')
        ax.spines['right'].set_color('none')
        ax.yaxis.set_visible(False)
        plt.savefig(fName)
        plt.show()

          ################################
          ###                          ###
          #  Basic bivariate statistics  #
          ###                          ###
          ################################

class BiSeries:
    #Constructor : (list1,list2) represents the bidimensional series
    def __init__(self, listX, listY, studyName, nX, nY):
        #Number of data
        self.size = len(listX)
        #One dimensional series X
        self.seriesX = listX
        #One dimensional series Y
        self.seriesY = listY
        #Sum of the elements for X
        self.sumX = sum(listX)
        #Mean of X
        self.meanX = self.sumX/self.size
        #Squared elements sum for X
        self.sumSquaresX = sum(np.square(listX))
        #Variance of X
        self.varX = self.sumSquaresX/self.size - self.meanX**2
        #Standard deviation of X
        self.stdDevX = sqrt(self.varX)
        #Ordered series for X
        self.orderSeriesX = sorted(listX)
        #Minimum of X
        self.minX = self.orderSeriesX[0]
        #Maximum of X
        self.maxX = self.orderSeriesX[self.size-1]
        #The scope of X
        self.scopeX = self.maxX - self.minX
        #Sum of the elements for Y
        self.sumY = sum(listY)
        #Mean of Y
        self.meanY = self.sumY/self.size
        #Squared elements sum for Y
        self.sumSquaresY = sum(np.square(listY))
        #Variance of Y
        self.varY = self.sumSquaresY/self.size - self.meanY**2
        #Standard deviation of Y
        self.stdDevY = sqrt(self.varY)
        #Ordered series for Y
        self.orderSeriesY = sorted(listY)
        #Minimum of Y
        self.minY = self.orderSeriesY[0]
        #Maximum of Y
        self.maxY = self.orderSeriesY[self.size-1]
        #Scope of Y
        self.scopeY = self.maxY - self.minY
        #Cross term sum
        s = 0
        for k in range(self.size):
            s = s + listX[k]*listY[k]
        self.cross = s
        #Covariance cov(X,Y)
        self.cov = self.cross/self.size - self.meanX*self.meanY
        #Linear correlation coefficient
        self.cc = self.cov/(self.stdDevX*self.stdDevY)
        #Slope for linear regression line
        self.theta1 = self.cov/self.varX
        #Ordinate at the origin for linear regression line
        self.theta0 = self.meanY - self.theta1*self.meanX
        #Study name
        self.sname = studyName
        #Name of X
        self.nameX = nX
        #Name of Y
        self.nameY = nY

"""
display
Arguments : fName is the backup file name
Return : empty
Process : print and save the scatterplot of the distribution
"""
    def display(self, fName):
        X = self.seriesX
        Y = self.seriesY
        fig = plt.figure(figsize = (10, 8))
        plt.xlim([self.minX - self.scopeX/10, self.maxX + self.scopeX/10])
        plt.ylim([self.minY - self.scopeY/10, self.maxY + self.scopeY/10])
        plt.title(self.sname)
        plt.xlabel(self.nameX)
        plt.ylabel(self.nameY)
        plt.grid(alpha =.6, linestyle =':')
        plt.plot(X, Y, "bD")
        #Rajouter un encadré avec du texte :
        #fig.text(0.8, 0.15, "Maxime Baczyk" ,fontsize = 15, color ='deepskyblue',ha ='right', va ='bottom',alpha = 0.7)
        plt.savefig(fName)
        plt.show()

"""
line
Arguments : fileName is the backup file nam
Return : empty
Process : print and save the scatterplot of the distribution and the regression line
"""
    def line(self, fName):
        X = np.linspace(self.minX - self.scopeX/10, self.maxX + self.scopeX/10, 150)
        Y = np.linspace(self.minY - self.scopeY/10, self.maxY + self.scopeY/10, 150)
        for k in range(0,150):
            Y[k] = self.theta1*X[k] + self.theta0
        fig = plt.figure(figsize = (10, 8))
        plt.plot(X, Y, "r-" ,linewidth=2.0)
        #plt.legend()
        plt.xlim([ self.minX - self.scopeX/10, self.maxX + self.scopeX/10 ])
        plt.ylim([ self.minY - self.scopeY/10, self.maxY + self.scopeY/10 ])
        plt.title("Affine fit :" + self.sname)
        plt.xlabel(self.nameX)
        plt.ylabel(self.nameY)
        plt.grid(alpha =.6, linestyle =':')
        ax = plt.gca()
        ax.plot(X, Y,"r-",linewidth=2.0)
        ax.grid(True)
        plt.plot(self.seriesX,self.seriesY,"bD")
        plt.savefig(fName)
        plt.show()
