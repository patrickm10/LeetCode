class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        diff1 = list(set1 - set2)
        diff2 = list(set2 - set1)

        return [diff1, diff2]
    
# Test

if __name__ == "__main__":
    s = Solution()
    print(s.findDifference([1,2,3], [2,4,6]))  # Output: [[1,3],[4,6]]
    print(s.findDifference([1,2,3,3], [1,2,4,5]))  # Output: [[3],[4,5]]
