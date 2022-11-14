def kClosest(points,k):
    distance =[((point[0]**2 + point[1]**2)**0.5,point[0],point[1]) for point in points]
    distance.sort()
    closest = [[distance[i][1],distance[i][2]] for i in range(k)]
    return closest



