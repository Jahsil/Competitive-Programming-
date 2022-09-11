def heapify(arr , curr , size):
    mx = curr
    l = 2 * curr + 1
    r = 2 * curr + 2
    
    if l < size and arr[l] > arr[mx]:
        mx = l
    if r < size and arr[r] > arr[mx]:
        mx = r
    if mx != curr:
        tmp = arr[curr]
        arr[curr] = arr[mx]
        arr[mx] = tmp
        
        heapify(arr , mx , size)

def buildHeap(arr):
    n = (len(arr)// 2) - 1
    for i in range(n,-1,-1):
        heapify(arr ,  i , len(arr) )
        
    return arr
def heapSort(arr):
    
    buildHeap(arr)
    
    n = len(arr)-1
    for i in range(n , -1 , -1):
        tmp = arr[0]
        arr[0] = arr[i]
        arr[i] = tmp
        
        heapify(arr , 0 , i)
        
    return arr
    
  
  
arr = [1,2,3,4,5,6,7,8,9]   
print("Given Array :--",arr)
print("Built heap :--",buildHeap(arr))
print("Sorted heap :--",heapSort(arr))
        
