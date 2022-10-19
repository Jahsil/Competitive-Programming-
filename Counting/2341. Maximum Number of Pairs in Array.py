class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pairsRemoved = 0
        numbersLeft = 0
        count = collections.Counter(nums)
        for x , y in count.items():
            while count[x] >= 2:
                count[x] -= 2
                pairsRemoved += 1

        for x , y in count.items():
            if count[x] != 0:
                numbersLeft += 1

        return [pairsRemoved , numbersLeft]
