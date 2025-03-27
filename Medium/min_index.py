class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Find the dominant element
        count = Counter(nums)
        dominant, total_count = max(count.items(), key=lambda x: x[1])
        
        left_count = 0
        
        for i, num in enumerate(nums[:-1]):
            if num == dominant:
                left_count += 1
            
            # Check if both left and right subarrays have the same dominant element
            if left_count > (i + 1) // 2 and (total_count - left_count) > (len(nums) - i - 1) // 2:
                return i
        
        return -1
