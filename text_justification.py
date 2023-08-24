"""
LeetCode
68. Text Justification
August 2023 Challenge
jramaswami
"""


from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # Divide words into lines.
        lines = []
        lengths = []
        curr_line = [words[0]]
        curr_length = len(words[0])
        for wd in words[1:]:
            # Be sure to add at least one word for spaces
            if curr_length + len(wd) + 1 > maxWidth:
                # If the word won't fit, move to the next line
                lines.append(curr_line)
                lengths.append(curr_length)
                curr_line = [wd]
                curr_length = len(wd)
            else:
                curr_line.append(wd)
                curr_length += (1 + len(wd))
        lines.append(curr_line)
        lengths.append(curr_length)

        soln = []
        for line, length in zip(lines[:-1], lengths[:-1]):
            if len(line) == 1:
                # A line with one word is left justified
                soln.append(line[0] + (" " * (maxWidth - len(line[0]))))
            else:
                # We already added a space between the words
                remaining_space = maxWidth - length
                # This space must be split as evenly as possible
                q, r = divmod(remaining_space, len(line) - 1)
                justified_line = []
                for wd in line[:-1]:
                    justified_line.append(wd)
                    spaces = 1 + q
                    # If there are any remaining spaces, put one here
                    if r > 0:
                        spaces += 1
                        r -= 1
                    justified_line.append(" " * spaces)
                # Put last word in place
                justified_line.append(line[-1])
                soln.append("".join(justified_line))
        # Add the last line, which is left justified
        justified_line = [" ".join(lines[-1])]
        remaining_space = maxWidth - len(justified_line[0])
        justified_line.append(" " * remaining_space)
        soln.append("".join(justified_line))
        return soln


def test_1():
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    expected = [
        "This    is    an",
        "example  of text",
        "justification.  "
    ]
    assert Solution().fullJustify(words, maxWidth) == expected


def test_2():
    words = ["What","must","be","acknowledgment","shall","be"]
    maxWidth = 16
    expected = [
        "What   must   be",
        "acknowledgment  ",
        "shall be        "
    ]
    assert Solution().fullJustify(words, maxWidth) == expected


def test_3():
    words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth = 20
    expected = [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  "
    ]
    assert Solution().fullJustify(words, maxWidth) == expected