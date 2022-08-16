class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        result = []
        for x , y in count.items():
            result.append(x * y)
        result.sort(reverse = True , key = self.lenOfItem)
        return "".join(result)
    
    def lenOfItem(self , i):
        return len(i)
            
