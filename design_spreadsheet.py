"""
LeetCode
3484. Design Spreadsheet
September 2025 Challenge
jramaswami
"""


import collections


class Spreadsheet:

    def __init__(self, rows: int):
        self.cells = collections.defaultdict(int)


    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        self.cells[cell] = 0

    def getValue(self, formula: str) -> int:
        left_ref, right_ref = formula[1:].split('+')
        if left_ref.isdigit():
            left_value = int(left_ref)
        else:
            left_value = self.cells[left_ref]
        if right_ref.isdigit():
            right_value = int(right_ref)
        else:
            right_value = self.cells[right_ref]
        return left_value + right_value


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)