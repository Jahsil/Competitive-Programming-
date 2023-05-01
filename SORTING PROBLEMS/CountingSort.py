nums = [5,4,8,5,7,1,2,9,5]
N = len(nums)
ans = [0] * N
count = [0] * N
print(count)
print("=================")
for i in range(0 , N - 1):
    for j in range(i + 1 , N):

        if nums[i] < nums[j]:
            count[j] = count[j] + 1
        else:
            count[i] = count[i] + 1
    print(count)
print("=======")
print(count)
for i in range(N):
    ans[count[i]] = nums[i]
print("Final count" , count)
print(ans)