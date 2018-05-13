# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 13:36:15 2018

@author: mai13
"""

import random,pylab

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    valid=0
    for i in range(numTrials):
        l=[0,0,0,1,1,1]
        for i in range(3):
            draw=random.choice(l)            
            l.remove(draw)
        if sum(l)==0 or sum(l) == 3:
            valid+=1
    return valid/numTrials

def testCLT(trial):
    result=[]
    for i in range (trial):
        result.append(noReplacementSimulation(1000))
    pylab.hist(result,bins=20,weights=pylab.array(len(result)*[1])/len(result))

testCLT(1000)