def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1
        merged.append(word1[i:])
        merged.append(word2[j:])
        return ''.join(merged)  # Return the merged string

# Test the solution
word1 = "abc"
word2 = "pqr"
solution = Solution()
result = solution.mergeAlternately(word1, word2)
print("Merged string:")
print(result)
