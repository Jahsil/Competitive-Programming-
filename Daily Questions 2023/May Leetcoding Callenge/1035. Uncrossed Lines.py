class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)

        has_cache = [[False] * n for _ in range(m)]
        cache = [[None] * n for _ in range(m)]
        

        def dfs(index1 , index2):
            if index1 == m or index2 == n:
                return 0

            if has_cache[index1][index2]:
                return cache[index1][index2]

            ans = 0
            if nums1[index1] == nums2[index2]:
                ans = max(ans , dfs(index1 + 1 , index2 + 1) + 1)
            ans = max(ans , dfs(index1 + 1 , index2) , dfs(index1 , index2 + 1))

            has_cache[index1][index2] = True
            cache[index1][index2] = ans
            return cache[index1][index2]

        return dfs(0 , 0)
