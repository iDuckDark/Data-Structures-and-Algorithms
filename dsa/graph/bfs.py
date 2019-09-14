"""breadth first search
References:
- https://en.wikipedia.org/wiki/Breadth-first_search
"""
from graph_examples import DIRECTED_GRAPH


def bfs(graph, start):
    """Breadth first search
    time: O(|V| + |E|)

    Args:
        graph (dict): graph
        start (node): some key of the graph
    """
    seen = set()
    path = []
    queue = [start]
    while queue:
        current = queue.pop(0)
        if current not in seen:
            seen.add(current)
            path.append(current)
            queue.extend(graph[current])
    return path


def test():
    """test"""
    assert bfs(DIRECTED_GRAPH, "C") == ["C", "A", "F", "B", "E", "D"]


if __name__ == "__main__":
    test()
