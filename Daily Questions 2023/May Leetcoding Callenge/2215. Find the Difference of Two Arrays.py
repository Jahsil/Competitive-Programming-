class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = []
        tmp = set()
        for num in nums1:
            if num not in nums2:
                tmp.add(num)
        ans.append(tmp)
        tmp = set()
        for num in nums2:
            if num not in nums1:
                tmp.add(num)
        ans.append(tmp)

        return ans
