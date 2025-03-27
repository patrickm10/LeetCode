class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            return -1 * self.reverse(-1 * x)
        else:
            reversed_int = int(str(x)[::-1])
            if reversed_int > 2**31 - 1:
                return 0
            else:
                return reversed_int
