class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        alphabets = [0] * 26
        for i , alphas in enumerate(s):
            alphabets[ord(alphas) - 97] = i
        
        start = 0 
        end = 0 
        result = []
        
        for i , alphas in enumerate(s):
            end = max(end, alphabets[ord(alphas) - 97])
            
            if i == end:
                result.append(end - start + 1)
                start = end + 1
        return result 
        
