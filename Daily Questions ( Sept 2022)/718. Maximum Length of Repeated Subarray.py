class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def findRepeated(nums1 , nums2):
            N1 = len(nums1)
            N2 = len(nums2)

            result = 0
            for i in range(N2):
                count = 0
                for j in range(N1):
                    if j + i >= N2:
                        break
                    if nums1[j] == nums2[j + i]:
                        count += 1
                        result = max(result , count)

                    else:
                        count = 0

            return result
        return max(findRepeated(nums1 , nums2),findRepeated(nums2 , nums1))
