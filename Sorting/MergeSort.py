class MergeSort:
    
    def dfs(self , arr):
        if len(arr) == 1:
            return arr
            
        mid = len(arr) // 2
        
        left = self.dfs(arr[0 : mid])
        right = self.dfs(arr[mid : ])
        
        return self.merge(left , right)
        
    def merge(self , left , right):
        i = 0
        j = 0 
        k = 0
        newArr = [0] * (len(left) + len(right))
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                newArr[k] = left[i]
                i += 1
            else:
                newArr[k] = right[j]
                j += 1
            k += 1
            
        while i < len(left):
            newArr[k] = left[i]
            i+= 1
            k += 1
            
        while j < len(right):
            newArr[k] = right[j]
            j+= 1
            k += 1
            
        return newArr
                
                
                
nums = [1,8,5,7,5,2,4,9,5,2,3,6]
m = MergeSort()
print(m.dfs(nums))
                
                
                
