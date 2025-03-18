class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        
        def expand_from_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            # Expand around the center for odd-length palindromes
            odd_palindrome = expand_from_center(i, i)
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            # Expand around the center for even-length palindromes
            even_palindrome = expand_from_center(i, i + 1)
            if len(even_palindrome) > len(longest):
                longest = even_palindrome
        
        return longest
