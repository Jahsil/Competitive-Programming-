class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        lookup = defaultdict(list)
        ans = 0

        for i in range(len(strs)):
            for j in range(len(strs[0])):
                lookup[j].append(ord(strs[i][j]))

        
        for k , v in lookup.items():
            val = -1
            for i in v:
                if i >= val:
                    val = i
                else:
                    ans += 1
                    break

        return ans
                
