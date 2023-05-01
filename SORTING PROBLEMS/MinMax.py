

def minmax(arr):
    start = 0
    end = len(arr) - 1
    mid = (start + end) // 2

    if end - start <= 1:
        if arr[start] < arr[end]:
            return (arr[start] , arr[end])
        else:
            return (arr[end] , arr[start])

    (a1 , b1) = minmax(arr[0 : mid])
    (a2 , b2) = minmax(arr[mid + 1 : ])
    minA = min(a1 , a2)
    maxB = max(b1 , b2)

    return (minA , maxB)

nums = [5,4,8,5,7,1,2,9,5]
print(minmax(nums))
