class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = OrderedDict(Counter(nums))
        count = dict( sorted(count.items(), key=operator.itemgetter(1),reverse=True))
       
        result = []
        
        for x , y in count.items():
            if k > 0:
                result.append(x)
                k -= 1
               
                
        return result
