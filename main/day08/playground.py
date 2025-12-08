import itertools
import math

get_distances = lambda j: sorted([((j1, j2), math.dist(j1, j2)) for j1, j2 in itertools.combinations(j, 2)],
                                 key=lambda x: x[1])


def solve_p1(junction_boxes, num_connections) -> int:
    distances = get_distances(junction_boxes)
    circuits = []
    for d in distances[:num_connections]:
        circuits = find_closest(d, circuits)
    return math.prod(len(c) for c in sorted(circuits, key=lambda x: -len(x))[:3])


def solve_p2(junction_boxes) -> int:
    distances = get_distances(junction_boxes)
    circuits = []
    i = 0
    while True:
        circuits = find_closest(distances[i], circuits)
        if len(circuits) == 1 and len(circuits[0]) == len(junction_boxes):
            return distances[i][0][0][0] * distances[i][0][1][0]
        i += 1


def find_closest(junction_pair, circuits):
    j1, j2 = junction_pair[0]
    j1_circuit, j2_circuit = None, None
    print()
    for i, c in enumerate(circuits):
        if j1 in c:
            j1_circuit = i
        if j2 in c:
            j2_circuit = i

    if j1_circuit is None and j2_circuit is None:
        circuits.append({j1, j2})
    elif j1_circuit is not None and j2_circuit is None:
        circuits[j1_circuit].add(j2)
    elif j2_circuit is not None and j1_circuit is None:
        circuits[j2_circuit].add(j1)
    elif j1_circuit is not None and j2_circuit is not None and j1_circuit != j2_circuit:
        circuits[j1_circuit].update(circuits.pop(j2_circuit))
    return circuits
