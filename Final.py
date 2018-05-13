# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 14:37:18 2018

@author: Haoyuan
"""
#%% Problem 2
import random, pylab
xVals = []
yVals = []
wVals = []
for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())
xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
wVals = pylab.array(wVals)
xVals = xVals + xVals
zVals = xVals + yVals
tVals = xVals + yVals + wVals
#pylab.plot(sorted(xVals),yVals)
#pylab.plot(zVals)
pylab.hist(tVals,10,lab)
#%% Problem 3
def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    valid=0
    for i in range(numTrials):
        l=[0,0,0,0,1,1,1,1]
        for i in range(3):
            draw=random.choice(l)            
            l.remove(draw)
        if sum(l)==1 or sum(l) == 4:
            valid+=1
    return valid/numTrials

drawing_without_replacement_sim(1000)
#%% Problem 4
import random, pylab
from itertools import groupby
# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values,numBins)
    if title!=None:
        pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.show()
    
makeHistogram([1,2], 4, "Aaa", "Bbb")                  
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    longruns=[]
    for i in range(numTrials):
        rollresult=[]
        for j in range(numRolls):
            rollresult.append(die.roll())            
        longruns.append(max(len(list(g)) for k, g in groupby(rollresult)))

    makeHistogram(longruns,10,'Longest Run','Times Occur')
    return round(getMeanAndStd(longruns)[0],3)
        
 # One test case
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))
#%% Problem 6 important!!!!!!!!!!!!!!!
import numpy as np
def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    subset=[]
    for i in range(2**len(choices)):
        subset.append(np.array(list('0'*(len(choices)-len(bin(i)[2:]))+bin(i)[2:]),dtype=int))
    print (subset[1])
    for array in subset:
        if np.dot(choices,array)==total:
            solution.append(array)
        elif len(solution)==0:
            
choice=[1,2,3,4]
find_combination(choice,4)
#%% Problem 8
import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    copyrabbitpop=CURRENTRABBITPOP
    if CURRENTRABBITPOP>10:
        for i in range(copyrabbitpop):
            if random.random()<=float(1-CURRENTRABBITPOP/MAXRABBITPOP):
                CURRENTRABBITPOP+=1
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    copyfoxpop=CURRENTFOXPOP
    if CURRENTFOXPOP>10:
        if CURRENTRABBITPOP>10:
            for i in range (copyfoxpop):
                if random.random()<=CURRENTRABBITPOP/MAXRABBITPOP:
                    CURRENTRABBITPOP-=1
                    if random.random()<=1/3.0:
                        CURRENTFOXPOP+=1
                else:
                    if random.random()<=9/10.0:
                        CURRENTFOXPOP-=1
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit,fox=[],[]
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit.append(CURRENTRABBITPOP)
        fox.append(CURRENTFOXPOP)
    pylab.plot(rabbit)
    pylab.plot(fox)
    coeffr = pylab.polyfit(range(len(rabbit)), rabbit, 2)
    pylab.plot(pylab.polyval(coeffr, range(len(rabbit))),label='rabbit')
    coefff = pylab.polyfit(range(len(fox)), fox, 2)
    pylab.plot(pylab.polyval(coefff, range(len(fox))),label='fox') 
    pylab.legend()
    return rabbit,fox

runSimulation(200)

        
    





