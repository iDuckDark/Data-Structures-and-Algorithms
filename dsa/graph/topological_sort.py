"""
Topological Sort

A topological sort of a directed graph is a linear ordering of its vertices
such that for every directed edge uv from vertex u to vertex v, u comes
before v in the ordering.

A topological ordering is possible if and only if the graph has no directed
cycles, that is, if it is a directed acyclic graph.

References:
- https://en.wikipedia.org/wiki/Topological_sorting
"""


def topological_sort_kahn(graph) -> list:
    """
    Kahn's algorithm for topological sort. Works by choosing vertices in the
    same order as the eventual topological sort. First, find a list of "start
    nodes" which have no incoming edges and insert them into a queue; at
    least one such node must exist in a non-empty acyclic graph

    Time: O(|V| + |E|)
    """
    ordering = []

    in_degree = {node: 0 for node in graph}
    for nodes in graph.values():
        for node in nodes:
            in_degree[node] += 1

    # set of all nodes with no incoming edges
    queue = [node for node, degree in in_degree.items() if degree == 0]

    while queue:
        current = queue.pop()
        ordering.append(current)
        for neighbour in graph[current]:
            in_degree[neighbour] -= 1
            if in_degree[neighbour] == 0:
                queue.append(neighbour)
    return ordering


def iterative_topological_sort(graph, start):
    """doesn't return some nodes"""
    seen = set()
    stack = []  # path variable is gone, stack and order are new
    order = []  # order will be in reverse order at first
    queue = [start]
    while queue:
        node = queue.pop()
        if node not in seen:
            seen.add(node)  # no need to append to path any more
            queue.extend(graph[node])

            while stack and node not in graph[stack[-1]]:  # new stuff here!
                order.append(stack.pop())
            stack.append(node)

    return stack + order[::-1]  # new return value!


def test():
    """run test cases"""
    graph = {
        "2": [],
        "3": ["8", "10"],
        "5": ["11"],
        "7": ["11", "8"],
        "8": ["9", "10"],
        "9": [],
        "10": [],
        "11": ["2", "9", "10"],
    }
    assert topological_sort_kahn(graph) == ["7", "5", "11", "2", "3", "8", "10", "9"]
    print(iterative_topological_sort(graph, "7"))


if __name__ == "__main__":
    test()
