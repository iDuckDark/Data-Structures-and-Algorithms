"""
References
Lucia Moura's CSI 2110 Chapter 19 Course Notes

Given a pattern, and an input string, give all the indices after which the pattern can
be found.

Example:
    Given input_string = "ABBCDDBCE", pattern = "BC",
    Because input_string[2:4] == input_string[6,8] == "BC"
    return 2, 6
"""


def _preprocess(pattern):
    """
    For each index in the pattern, determine how many characters counting from the start
    of the pattern are "simulatenously matched" (aka length of prefix suffix if the
    string ended at that index).

    Example:
        pattern = "abaaba"
        result = [0, 0, 1, 1, 2, 3]

    If we have a match up to index 2 or 3, we also simulatenously matched up to index 0,
    since index 0, 2, 3 are all "a".
    Similarly, if we match up to index 5, we have index 3, 4, 5 which make up "aba"
    allowing us to simulateously match up to index 2.

    time: O(m)
    space: O(m)
    where m is the size of the pattern.
    """
    result = [0]
    # i is the current index of the pattern being preprocessed.
    i = 1
    # j stores the maximum value of the previous match (the maximum simulatenously match
    # of the previous index).
    j = 0
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            # We have one more match than the previous value.
            result.append(j + 1)
            j += 1
            i += 1
        elif j > 0:
            # There isn't a match: we lower j to be the value of the next maximum
            # simulatanous match.
            j = result[j - 1]
        else:
            # The maximum simulatenous match is 0, and we don't have a  match witrh the
            # first character of the pattern. We have no "simulatenous match."
            result.append(0)
            i += 1
    return result


def knuth_morris_pratt(input_string, pattern):
    """
    time: O(mn)
    space: O(m)
    note although the upperbound is the same as the brute force solution, it performs
    better when the pattern is long and "contains repetitions."
    """
    # When there are "repetitions," we could be simulatenously matching different parts
    # of the same pattern. When one match fails, we call the failure_function and
    # move on to the next highest simultaneous match.
    failure_function = _preprocess(pattern)
    i = j = 0
    while i < len(input_string):
        if input_string[i] == pattern[j]:
            if j == len(pattern) - 1:
                # Reached the end of the pattern, return a match, and continue.
                yield i - j
                j = failure_function[j]
                i += 1
            else:
                # Not yet the end of the pattern, continue checking next character.
                i += 1
                j += 1
        else:
            if j > 0:
                # Move on to the next highest "simulatenous match."
                j = failure_function[j - 1]
            else:
                i += 1
