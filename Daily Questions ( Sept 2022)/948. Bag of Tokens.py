class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        result = 0 
        tokens.sort()
        
        a_pointer = 0
        b_pointer = len(tokens) - 1
        
        while a_pointer <= b_pointer:
            
            if power >= tokens[a_pointer]:
                
                score += 1
                power -= tokens[a_pointer]
                result = max(result , score)
                a_pointer += 1
                
            else:
                if score >= 1:
                    power += tokens[b_pointer]
                    score -= 1
                    b_pointer -= 1
                else:
                    break
            
        return result
        
