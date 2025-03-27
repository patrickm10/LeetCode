class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if numRows is 1 or greater than or equal to string length, return original string
        if numRows == 1 or numRows >= len(s):
            return s

        # Initialize a list of strings for each row
        rows = [''] * numRows
        current_row = 0  # Track current row index
        going_down = False  # Direction flag

        # Iterate over each character in the input string
        for char in s:
            rows[current_row] += char  # Add character to the current row
            # Change direction at the top and bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            # Move up or down
            current_row += 1 if going_down else -1

        # Combine all rows to get the final result
        return ''.join(rows)
