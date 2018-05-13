# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 14:11:16 2018

@author: mai13
"""

def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    trip=[]
    trips=[]
    copy_cows=sorted(cows.items(),key= lambda x:x[1])
    print(copy_cows)
    while len(copy_cows)>0:
        for item in copy_cows[:]:
            if copy_cows[-1][1]<limit:
                trip.append(item[-1][0])
                limit-=copy_cows[-1][0]
                copy_cows.pop()
        trips.append(trip)
        trip=[]
        limit=10
    return trips
        
    