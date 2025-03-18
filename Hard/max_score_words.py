class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letter_count = [0] * 26
        for ch in letters:
            letter_count[ord(ch) - ord('a')] += 1

        word_scores = []
        word_counts = []
        for word in words:
            word_count = [0] * 26 
            word_score = 0
            for ch in word:
                idx = ord(ch) - ord('a')
                word_count[idx] += 1
                word_score += score[idx]
            word_scores.append(word_score)
            word_counts.append(word_count)

        def dfs(idx, remaining):
            if idx == len(words):
                return 0
            
            # Skip the current word
            max_score = dfs(idx + 1, remaining)

            if all(remaining[i] >= word_counts[idx][i] for i in range(26)):
                
                for i in range(26):
                    remaining[i] -= word_counts[idx][i]
                max_score = max(max_score, word_scores[idx] + dfs(idx + 1, remaining))
                
                for i in range(26):
                    remaining[i] += word_counts[idx][i]

            return max_score

        return dfs(0, letter_count)
