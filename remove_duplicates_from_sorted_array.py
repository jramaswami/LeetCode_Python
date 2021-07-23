"""
LeetCode :: Array Module :: Remove Duplicates from Sorted Array
jramaswami
"""


class Solution:
    def removeDuplicates(self, A):
        # Init
        read_index = write_index = 1
        removed = 0

        # Loop while read_index is inbounds.
        while read_index < len(A):
            # Find the first value that does not equal
            # the previous value
            while read_index < len(A) and A[read_index] == A[write_index - 1]:
                read_index += 1
                removed += 1

            if read_index < len(A):
                # If the read index is still inbounds
                # write value to write index.
                A[write_index] = A[read_index]

            read_index += 1
            write_index += 1

        # When done return the "length" of the new array
        return len(A) - removed
