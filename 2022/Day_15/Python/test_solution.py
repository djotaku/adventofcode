from . import solution


def test_extra_coordinates():
    test_string = "Sensor at x=2, y=18: closest beacon is at x=-2, y=15"
    coordinates = solution.extract_coordinates(test_string)
    assert coordinates[0].x == 2
    assert coordinates[1].x == -2
    assert coordinates[0].y == 18
    assert coordinates[1].y == 15


def test_calculate_taxi_distance():
    sensor = solution.Coordinate(8, 7)
    beacon = solution.Coordinate(2, 10)
    taxi_distance = solution.calculate_taxi_distance(sensor, beacon)
    assert taxi_distance == 9


def test_find_beacon_exclusion_zone():
    sensor = solution.Coordinate(8, 7)
    beacon = solution.Coordinate(2, 10)
    taxi_distance = 9
    no_beacons = solution.find_beacon_exclusion_zone(sensor, taxi_distance, beacon)
    assert solution.Coordinate(8, -2) in no_beacons
    assert solution.Coordinate(8, 16) in no_beacons
