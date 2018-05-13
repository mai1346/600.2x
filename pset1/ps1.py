###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
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
#    trip=[]
#    trips=[]
#    copy_cows=cows.copy()
#    maxcow=''
#    while True:
#        try:
#            while min(copy_cows.values())<limit:
#                for cow in copy_cows.keys():
#                    if copy_cows[cow]<=limit:
#                        if copy_cows[cow]>=copy_cows.get(maxcow,0):
#                            maxcow=cow            
#                trip.append(maxcow)         
#                limit-=copy_cows[maxcow]
#                del copy_cows[maxcow]   
##                print('maxcow= %s, limit= %d' % (maxcow, limit))
#                if len(copy_cows)==0:
#                    break       
#            trips.append(trip)
#            trip=[]
#            limit=10
##            print(trips)
#        except:
#            break         
#    return trips
    
#    i=0
#    trips=[[] for_ in enumerate(cows)]
#    newcow=[]
#    totalcost=0
#    copy_cows=sorted(cows.items(),key= lambda x:x[1],reverse=True)
##    print(copy_cows)
#    while True:  
#        trips[i].append(item[0])
##        for item in copy_cows[:]:
##            if item[1]<=limit:
##                trip.append(item[0])
##                limit-=item[1]
##        trips[i].append(trip)
##        trip=[]
##        limit=10
##    return trips   
    temp=limit   
    trip=[]
    trips=[]
    copy_cows=sorted(cows.items(),key= lambda x:x[1],reverse=True)
    while len(copy_cows)>0:       
        for item in copy_cows[:]:
            if item[1]<=limit:
                trip.append(item[0])
                limit-=item[1] #update the limit
                copy_cows.remove(item) #update the list by deleting the item valid
        trips.append(trip)
        trip=[]
        limit=temp
    return trips 


            


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
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
    # get the total weight of cows in the partition
    totallist=[] #use a list to store the total weight of every trip of trips
    validtrips=[]
    for item in (get_partitions(cows)): 
        totallist=[] #reset the list for every item in generater
        for trip in item:
#            print('trip=',trip)
            total=0 #reset the sum for every single trip
            for cow in trip:
                total+=cows[cow]
            totallist.append(total)
#        print(totallist)
        ## To find the item that made of least trips(item with the smallest len())
        if max(totallist)<=limit:
            validtrips.append(item) #store valid trips obtained by brute force
        lenlist=[len(item) for item in validtrips] #
    ## return the optimal item
    for item in validtrips:
        if len(item)==min(lenlist):
            return item 

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    start1 = time.time()
    print(greedy_cow_transport(cows, limit))
    end1 = time.time()
    print(end1 - start1)
    start = time.time()
    print(brute_force_cow_transport(cows, limit))
    end = time.time()
    print(end - start)


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
#print(cows)
#
#print(greedy_cow_transport(cows, limit))
#print(brute_force_cow_transport(cows, limit))
#for item in (get_partitions(cows)):
#     print(item)
compare_cow_transport_algorithms()




