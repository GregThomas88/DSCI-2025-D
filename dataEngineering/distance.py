import googlemaps
import time

def distCalc(x, y):
    file = open("gMapsAPIKey.txt")
    gMapsKey = file.read()
    file.close()

    gmaps = googlemaps.Client(key=gMapsKey)

    distance = gmaps.distance_matrix(x, y)['rows'][0]['elements'][0]

    try:
        val = distance['distance']['text']
    except:
        val = r'\N'
    
    return(val)


def createDistanceData(data):
    fullDistList = []
    i = 0
    min, max = 0, 10
    while (i <= (len(data.index)/10)):
        distanceList = []
        for idx in range(min, max):
                distanceList.append(distCalc(data['SRCNAME'][idx], data['DESTINNAME'][idx]))
        fullDistList.append(distanceList)
        i = i + 1
        min = max
        max = max + 10
        time.sleep(2)

distCalc('Jorge Chávez International Airport', 'Patreksfjörður Airport')