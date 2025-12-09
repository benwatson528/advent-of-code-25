import itertools

from shapely.geometry.polygon import Polygon


def solve_p1(red_tiles) -> int:
    return sorted(
        [((p1, p2), (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)) for p1, p2 in
         itertools.combinations(red_tiles, 2)],
        key=lambda x: -x[1])[0][1]


def solve_p2(red_tiles) -> int:
    polygon = Polygon(red_tiles)
    max_area = 0
    for c1, c2 in itertools.combinations(red_tiles, 2):
        min_x, max_x = min(c1[0], c2[0]), max(c1[0], c2[0])
        min_y, max_y = min(c1[1], c2[1]), max(c1[1], c2[1])
        rectangle = Polygon([(min_x, min_y), (max_x, min_y), (max_x, max_y), (min_x, max_y)])
        if polygon.contains(rectangle):
            max_area = max(max_area, ((max_x - min_x) + 1) * ((max_y - min_y) + 1))
    return max_area
