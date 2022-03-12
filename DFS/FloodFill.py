class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        a = image[sr][sc]
        def dfs(rw , cl):
            nonlocal m , n , newColor , image
            if rw < 0 or rw > m-1 or cl < 0 or cl > n-1 or image[rw][cl] == newColor or image[rw][cl] != a:
                return 
            image[rw][cl] = newColor
            dfs(rw-1 , cl)
            dfs(rw+1 , cl)
            dfs(rw , cl+1)  
            dfs(rw , cl-1)
        dfs(sr , sc)
        return image
            
