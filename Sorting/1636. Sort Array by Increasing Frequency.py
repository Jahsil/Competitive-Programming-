class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        freq = sorted(freq.items() , key = lambda x : (x[1] ,-x[0]))
        arr = []
        for x , y in freq:
            arr.extend([x] * y)
        return arr
