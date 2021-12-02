from helper import distance

f = open("cities.csv", "r", encoding="utf-8")

points = []
for line in f.readlines():
    seperated = line.strip().split(",")[-1]
    point = seperated.replace("(", "").replace(
        ")", "").replace("Point", "").split(" ")
    points.append([point[0], point[1]])
points.append([0, 90])

distanceTraveled = 0
currentPoint = [0, 90]
currentClosestPoint = currentPoint
while len(points) > 0:
    currentClosestDistance = 999999
    for point in points:
        calculatedDistance = distance(
            currentPoint[1], point[1], currentPoint[0], point[0])
        if(calculatedDistance < currentClosestDistance):
            currentClosestDistance = calculatedDistance
            currentClosestPoint = point
    distanceTraveled += currentClosestDistance
    currentPoint = currentClosestPoint
    points.remove(currentClosestPoint)
distanceTraveled += distance(currentPoint[1], 90, currentPoint[0], 0)
print(distanceTraveled)
