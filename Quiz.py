# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 07:51:28 2018

@author: Haoyuan
"""
print(4%5)
#%% Problem 3
def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    m=[]
    for i in L:
        m.append(s//i)
        s=s%i
    if s!=0:
        return 'no solution'
    else:
        return sum(m)
a=[5,3,2]
s=11
greedySum(a,s)
#%% Problem 4
def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    sums=[]
    for i in range(len(L)):
        for j in range(i,len(L)):
            subsum=sum(L[i:j+1])
            sums.append(subsum)
    return max(sums)
L= [3, 4, -8, 15, -1, 2]
max_contig_sum(L)
#%% Problem 7
def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    i=0
    while not test(i) and not test(-i):
        i+=1
    if test(i):
        return i
    if test(-i):
        return -i

#### This test case prints 49 ####
def f(x):
    return (x+15)**0.5 + x**0.5 == 15
print(solveit(f))

#### This test case prints 0 ####
def f(x):
    return x == -80
print(solveit(f))

            
            
