"""
https://leetcode.com/problems/longest-common-prefix/

Find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

["flower","flow","flight"] -> "fl"
"""


def common_prefix(strings) -> str:
    """
    get first and last string by alphabetical sorting and return the common prefix
    time: O(n)
    space: O(1)
    """
    if not strings:
        return ""
    first = min(strings)  # first string by alphabetical sorting
    last = max(strings)  # last string by alphabetical sorting
    for i, char in enumerate(first):
        if char != last[i]:
            return first[:i]
    return first
