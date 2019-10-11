"""
Prim's algorithm is a greedy algorithm that finds a minimum spanning tree for a
weighted undirected graph

References:
- https://en.wikipedia.org/wiki/Prim%27s_algorithm
- https://bradfieldcs.com/algos/graphs/prims-spanning-tree-algorithm/
"""
from collections import defaultdict
from heapq import heapify, heappop, heappush
from pprint import pprint


def prim(graph):
    """Prim's algorithm
    graph should have at least one node
    Time: O(|E|log|V|)
    """
    start = next(iter(graph))  # get arbitrary node from graph
    visited = {start}
    min_span_tree = defaultdict(dict)

    # priority queue of edges
    edges = [(cost, start, end) for end, cost in graph[start].items()]
    heapify(edges)
    while edges:
        cost, start, end = heappop(edges)
        if end not in visited:
            visited.add(end)
            min_span_tree[start][end] = cost

            for to_next, cost in graph[end].items():
                if to_next not in visited:
                    heappush(edges, (cost, end, to_next))
    return min_span_tree


def test():
    """run test cases"""

    example_graph = {
        "A": {"B": 2, "C": 3},
        "B": {"A": 2, "C": 1, "D": 1, "E": 4},
        "C": {"A": 3, "B": 1, "F": 5},
        "D": {"B": 1, "E": 1},
        "E": {"B": 4, "D": 1, "F": 1},
        "F": {"C": 5, "E": 1, "G": 1},
        "G": {"F": 1},
    }

    pprint(prim(example_graph))


if __name__ == "__main__":
    test()
