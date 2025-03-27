
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        res = []
        self.dfs(digits, phone, 0, '', res)
        return res

    def dfs(self, digits: str, phone: dict, index: int, path: str, res: List[str]):
        if index == len(digits):
            res.append(path)
            return
        for char in phone[digits[index]]:
            self.dfs(digits, phone, index + 1, path + char, res)
