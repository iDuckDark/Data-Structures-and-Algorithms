"""depth first search

References
- https://en.wikipedia.org/wiki/Depth-first_search
"""
from graph_examples import DIRECTED_GRAPH


def dfs(graph, start):
    """Depth first search
    Args:
        graph (dict): graph
        start (node): some key of the graph
    """
    seen = set()
    path = []
    stack = [start]
    while stack:
        current = stack.pop()
        if current not in seen:
            seen.add(current)
            path.append(current)
            stack.extend(graph[current])
    return path


def test():
    """run test cases"""
    dfs(DIRECTED_GRAPH, "C")


if __name__ == "__main__":
    test()
