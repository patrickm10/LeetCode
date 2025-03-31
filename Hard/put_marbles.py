
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        
        if k == 1:
            return 0
        
        if k == n:
            return 0
        
        # Calculate the pair sums.
        pair_sums = [weights[i] + weights[i + 1] for i in range(n - 1)]
        
        # To maximize the score, we need the largest (k-1) pair sums.
        # To minimize the score, we need the smallest (k-1) pair sums.
        pair_sums.sort()
        max_score = sum(pair_sums[-(k - 1):])
        min_score = sum(pair_sums[:k - 1])

        return max_score - min_score
