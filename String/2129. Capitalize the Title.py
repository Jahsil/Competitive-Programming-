class Solution:
    def capitalizeTitle(self, title: str) -> str:
        ans = []
        
        for i in title.split(" "):
            if len(i) <= 2:
                ans.append(i.lower())
            else:
                ans.append(i[0].upper() + i[1:].lower())
                
        return " ".join(ans)
