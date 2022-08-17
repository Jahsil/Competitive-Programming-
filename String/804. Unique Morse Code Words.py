class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result = set()
        for word in words:
            morse_transformation = ""
            for letter in word:
                morse_transformation += morse[ord(letter) - 97]
            result.add(morse_transformation)
            
        return len(result)
                
        
