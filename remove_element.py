"""
LeetCode :: Array Module :: Remove Element
jramaswami
"""


class Solution:
    def removeElement(self, A, val):
        i = 0  # write index
        j = 0  # read index
        k = 0  # removed elements

        while i < len(A):
            # If read index points to val, move read index forward and
            # record the "removal" of the element.
            while j < len(A) and A[j] == val:
                j += 1
                k += 1

            # If read index is inbounds, write the value at the read index
            # to the cell at the write index.
            if j < len(A):
                A[i] = A[j]

            i += 1
            j += 1

        # Return the number of elements removed.
        return len(A) - k
