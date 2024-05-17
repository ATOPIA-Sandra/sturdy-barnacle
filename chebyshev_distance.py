#...............................exercice 40.........................
#first implementation of the function chebyshev_distance
def chebyshev_distance(point1, point2):
    return max(abs(a-b) for a, b in zip(point1,point2))



#second implementation of the function chebyshev_distance

def chebyshev_distance(point1, point2):
    max_distance =0
    for a, b in zip(point1, point2):
        max_distance = max(max_distance, abs(a-b))
    return max_distance


