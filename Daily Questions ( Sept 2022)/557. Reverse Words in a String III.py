class Solution:
    def reverseWords(self, s: str) -> str:
        arr = []
        for word in s.split():
            arr.append(word[::-1] + " ")
        for i in range(len(arr)):
            if i == (len(arr) - 1):
                arr[i] = arr[i].rstrip()
        return "".join(arr)
        
        
        
