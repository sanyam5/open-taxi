from geopy.distance import vincenty

def distance_km(coord1, coord2):
    return euclid_distance_km(coord1, coord2)

def euclid_distance_km(coord1, coord2):
    return vincenty(coord1, coord2).km

def road_distance_km(coord1, coord2):
    return 0
