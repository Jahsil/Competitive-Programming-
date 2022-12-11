class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = [l for i , l in enumerate(s.lower()) if l.isalpha() or l.isnumeric()]
        newS = "".join(newS)
        return newS == newS[::-1]
