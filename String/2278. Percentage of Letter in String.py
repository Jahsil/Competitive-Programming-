class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return int((sum(v for k , v in Counter(s).items() if letter == k) / len(s)) * 100)
