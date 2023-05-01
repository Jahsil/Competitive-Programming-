nums = [5,4,8,5,7,1,2,9,5]
N = len(nums)

start = 0
end = N - 1
key = 78
j = -1

while start <= end:
    mid = start + (end - start)//2
    if key == nums[mid]:
        j = mid
        break

    elif key < nums[mid]:
        end = mid - 1
    else:
        start = mid + 1

print(j)

