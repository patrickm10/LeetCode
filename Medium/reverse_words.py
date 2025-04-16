class Solution:
    def reverseWords(self, s: str) -> str:
        strs = s.split()
        return ' '.join(strs[::-1])
    

# Test

if __name__ == "__main__":
    s = Solution()
    print(s.reverseWords("The sky is blue")) # Output: "blue is sky The"
