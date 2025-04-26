# Imports
import networkx as nx
import pandas as pd

def findRoutes (dataSet, startAirport, endAirport, cutoff):
    # Create the network so that we can get our additional routes that could be used to get from our start to finish
    G = nx.from_pandas_edgelist(dataSet, 'SRCIATA', 'DESTINIATA', create_using=nx.DiGraph())

    # Set up the data set to have distance values (as the crow flies) to be able to do hierarchical clustering in regards to the amount of stops and total distance for the route.
    routes = pd.DataFrame({"PATH": [], "STOPS": [], "TOTAL_DIST": [], "TOTAL_TIME": []})

    paths = nx.all_simple_paths(G, startAirport, endAirport, cutoff=cutoff)
    for path in paths: # Let's work only with data that would only result in 2 or less additional airport stops
        nodeLocation = 0
        totalDistance = 0
        totalTime = 0
        for index in path:
            # Calculate total distance and time of the route
            currentIATA = index
            if nodeLocation != 0:
                totalDistance = totalDistance + (dataSet.loc[(dataSet['SRCIATA'] == pastIATA) & (dataSet['DESTINIATA'] == currentIATA), 'meters'].values)[0]
                totalTime = totalTime + (dataSet.loc[(dataSet['SRCIATA'] == pastIATA) & (dataSet['DESTINIATA'] == currentIATA), 'seconds'].values)[0]
            nodeLocation = nodeLocation + 1
            pastIATA = index
        totalTime = totalTime + ((len(path) - 2) * (60 * 90)) # Penalize routes with connections to account for layover time. Giving a flat 90 minutes of average layover time for each additional stop.
        
        # Keep track of the highest score to assign to the optimal route
        routes_Entry = pd.DataFrame({"PATH": [path], "STOPS": [len(path) - 2], "TOTAL_DIST": [totalDistance], "TOTAL_TIME": [totalTime]})
        routes = pd.concat([routes, routes_Entry])

    return(routes)


# Test
usRoutes_csv = pd.read_csv('C:/Users/joell/OneDrive/Capstone/DSCI-2025-D/data/usRoutesClean2.csv')

print(findRoutes(usRoutes_csv, 'LAX', 'ATL', 2))