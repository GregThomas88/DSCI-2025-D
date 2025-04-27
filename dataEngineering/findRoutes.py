# Imports
import networkx as nx
import pandas as pd

# PARAMETERS
# dataSet:          Must have SRCIATA, DESTINIATA, meters columns in it to work.
# startAirport      The airport that you are starting at.
# endAirport        The airport that you are trying to get to.
# cutoff            How many airports are you will to go to in order to find the shortest route before giving up?
#                       A value of one means you are only willing to go to 1 aka your end airport...
#                       So passing a value of 1 will only return direct flights if they exist. 

def findRoutes (dataSet, startAirport, endAirport, cutoff):
    # Create the network so that we can get our additional routes that could be used to get from our start to finish
    G = nx.from_pandas_edgelist(dataSet, 'SRCIATA', 'DESTINIATA', create_using=nx.DiGraph())

    cutoffValue = 0     # Used to track what depth the while loop is at
    noRoute = True      # Used to track if a route was found and the loop can be stopped early

    while (cutoffValue <= cutoff) & (noRoute == True):  # Loop goes through and finds the shallowest depth that we can work with
        cutoffValue = cutoffValue + 1
        paths = nx.all_simple_paths(G, startAirport, endAirport, cutoff=cutoffValue)

        for path in paths:
            noRoute = False

    if cutoffValue > cutoff:
        return("NO_PATH")

    paths = nx.all_simple_paths(G, startAirport, endAirport, cutoff=cutoffValue)

    shortestTotalDistance = 0   # Used to track what the shortest total distance is for later comparison of ranking 

    for path in paths: 
        nodeLocation = 0
        totalDistance = 0
        potentialRoute = pd.DataFrame({"SRC": [], "DESTIN": [], "METERS": []})

        for index in path:
            # Calculate total distance of the route
            currentIATA = index
            if nodeLocation != 0:
                distance = (dataSet.loc[(dataSet['SRCIATA'] == pastIATA) & (dataSet['DESTINIATA'] == currentIATA), 'meters'].values)[0]
                totalDistance = totalDistance + distance
                indexEntry = pd.DataFrame({"SRC": [pastIATA], "DESTIN": [currentIATA], "METERS": [distance]})
                potentialRoute = pd.concat([potentialRoute, indexEntry])

            nodeLocation = nodeLocation + 1
            pastIATA = index
        
        if shortestTotalDistance == 0:                  # Takes the first value found a promotes it to the shortest
            shortestTotalDistance = totalDistance
            shortestRoute = potentialRoute.copy()
        else:
            if shortestTotalDistance > totalDistance:   # Compares the shortest with the current to see if it needs to replace
                shortestTotalDistance = totalDistance
                shortestRoute = potentialRoute.copy()

    return(shortestRoute)


# Testing
usRoutes_csv = pd.read_csv('C:/Users/joell/OneDrive/Capstone/DSCI-2025-D/data/usRoutesClean2.csv')

print("Test 1 for MSY to IND")
print(findRoutes(usRoutes_csv, 'MSY', 'IND', 4))

print("\n\nTest 2 for FLL to MEM")
print(findRoutes(usRoutes_csv, 'FLL', 'MEM', 4))

print("\n\nTest 3 for FLL to MEM with constraint of no stops")
print(findRoutes(usRoutes_csv, 'FLL', 'MEM', 1))

print("\n\nTest 4 for LAX to ATL, to show direct flight behavior")
print(findRoutes(usRoutes_csv, 'LAX', 'SFO', 5))