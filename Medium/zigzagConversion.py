class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        current_row = 0  # Track current row index
        going_down = False  # Direction flag

        for char in s:
            rows[current_row] += char  # Add character to the current row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            # Move up or down
            current_row += 1 if going_down else -1

        return ''.join(rows)
