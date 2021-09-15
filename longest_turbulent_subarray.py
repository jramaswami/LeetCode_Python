"""
LeetCode :: September 2021 Challenge :: Longest Turbulent Subarray
jramaswami
"""

class Solution:

    def maxTurbulenceSize(self, arr):

        def sign(x):
            """Return the sign of x."""
            if x < 0:
                return -1
            elif x > 0:
                return 1
            return 0

        def traverse(start_index):
            """Traverse array while it is still turbulent."""
            # If we go over, then that is the end.
            if start_index + 1 >= len(arr):
                return start_index + 1
            # Get the first delta
            prev_delta = sign(arr[start_index] - arr[start_index + 1])
            # Get the remaining deltas from the right.
            curr_index = start_index + 1
            if curr_index + 1 >= len(arr):
                return curr_index + 1
            curr_delta = sign(arr[curr_index] - arr[curr_index + 1])
            while curr_delta != 0 and prev_delta != curr_delta:
                curr_index += 1
                if curr_index + 1 >= len(arr):
                    break
                prev_delta, curr_delta = curr_delta, sign(arr[curr_index] - arr[curr_index + 1])

            return curr_index + 1

        # See how far you can get from each starting index.
        soln = 1
        start_index = 0
        while start_index < len(arr):
            end_index = traverse(start_index)
            soln = max(soln, end_index - start_index)
            if end_index - 1 != start_index:
                start_index  = end_index - 1
            else:
                start_index = end_index
        return soln


def test_1():
    arr = [9,4,2,10,7,8,8,1,9]
    assert Solution().maxTurbulenceSize(arr) == 5


def test_2():
    arr = [4,8,12,16]
    assert Solution().maxTurbulenceSize(arr) == 2


def test_3():
    arr =   [100]
    assert Solution().maxTurbulenceSize(arr) == 1


def test_4():
    """WA"""
    arr = [9, 9]
    assert Solution().maxTurbulenceSize(arr) == 1


def main():
    """Test against a really long array."""
    import random
    arr = [random.randint(0, pow(10, 9)) for _ in range(4 * pow(10, 4))]
    print(Solution().maxTurbulenceSize(arr))

    arr = [0, 1] * (2 * pow(10, 4))
    print(Solution().maxTurbulenceSize(arr))


if __name__ == '__main__':
    main()

