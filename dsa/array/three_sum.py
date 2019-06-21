""" three values that sum to x """


def three_sum_bf(arr, target=0):
    """
    O(n^3)
    """
    result = []
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1, len(arr)):
                if arr[i] + arr[j] + arr[k] == target:
                    result.append((arr[i], arr[j], arr[k]))
    return result
