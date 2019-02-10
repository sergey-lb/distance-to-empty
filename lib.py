def calculate_distance_to_empty(consumption_per_100_km, fuel_level):
    """

    >>> calculate_distance_to_empty(10, 10)
    100

    >>> calculate_distance_to_empty(10, 5)
    50
    """

    consumption_per_km = consumption_per_100_km/100
    distance_to_empty = fuel_level/consumption_per_km
    distance_to_empty = int(distance_to_empty // 1)
    return distance_to_empty
