"""
find three values that sum to x
"""


def three_sum_naive(arr, target=0):
    """
    O(n^3)
    """
    result = set()
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1, len(arr)):
                if arr[i] + arr[j] + arr[k] == target:
                    result.add((arr[i], arr[j], arr[k]))
    return result


def three_sum_closest(nums, target):
    """
    Return total closest to target
    Worst case: O(n^2)
    """
    nums.sort()  # sort nums to perform two pointers
    result = sum(nums[:3])  # initial sum
    for i, _ in enumerate(nums):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if abs(total - target) < abs(result - target):
                result = total

            if total < target:  # move left pointer rightward for larger val
                left += 1
            elif total > target:  # move right pointer leftward for smaller val
                right -= 1
            else:  # if total == target, we can directly return
                return result
    return result


def three_sum(arr):
    """O(n^2)
    Compact, but slow on arrays with many duplicates
    """
    result = set()
    arr.sort()

    for i in range(len(arr) - 2):
        start = i + 1
        end = len(arr) - 1

        while start < end:
            if arr[i] + arr[start] + arr[end] == 0:
                result.add((arr[i], arr[start], arr[end]))
            if arr[i] + arr[start] + arr[end] < 0:
                start += 1
            else:
                end -= 1

    return result


def three_sum_fast(arr):
    """O(n^2)"""
    result = []
    arr.sort()

    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        start = i + 1
        end = len(arr) - 1

        while start < end:
            if arr[i] + arr[start] + arr[end] == 0:
                result.append((arr[i], arr[start], arr[end]))
            if arr[i] + arr[start] + arr[end] < 0:
                current_start = start
                while arr[start] == arr[current_start] and start < end:
                    start += 1
            else:
                current_end = end
                while arr[end] == arr[current_end] and start < end:
                    end -= 1
    return result


def test():
    """run test cases"""
    tests = (([-1, 0, 1, 2, -1, -4], 2),)
    for arg, result in tests:
        print(three_sum(arg))
        print(three_sum_fast(arg))
        print(three_sum_naive(arg))
        assert len(three_sum(arg)) == result
        assert len(three_sum_fast(arg)) == result
        assert len(three_sum_naive(arg)) == result


if __name__ == "__main__":
    test()
