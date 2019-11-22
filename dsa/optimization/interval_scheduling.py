"""
Interval scheduling.

References:
    https://en.wikipedia.org/wiki/Interval_scheduling
"""
from operator import itemgetter


def greedy_scheduling(jobs) -> int:
    """
    Greedy interval schedule
    Time: O(n)
    """
    # jobs, sorted by earliest finishing time
    sorted_jobs = sorted(jobs, key=itemgetter(1))
    n_jobs = 0
    last_end = 0
    for start, end in sorted_jobs:
        if start >= last_end:
            last_end = end
            n_jobs += 1
    return n_jobs


def test():
    """run test cases"""
    # [0, 1] -> start, finish
    test_cases = (([[0, 1], [1, 2], [2, 3], [2, 5]], 3),)
    for arg, expected in test_cases:
        assert greedy_scheduling(arg) == expected


if __name__ == "__main__":
    test()
