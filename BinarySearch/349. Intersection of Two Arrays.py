class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = set(nums1)
        n2 = set(nums2)
        ans = []
        for num in n1:
            if num in n2:
                ans.append(num)
                
        return ans
