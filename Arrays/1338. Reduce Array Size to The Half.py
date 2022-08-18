class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        count = sorted(count.items() , key = lambda z: -z[1])
        print(count)
        length = len(arr)
        value = 0
        result = 0
        
        for x , y in count:
            value += y
            result += 1
            if value >= length//2:
                break
        
        return result
        
        
        
