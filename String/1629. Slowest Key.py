class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        arr = [0] * len(releaseTimes)
        arr[0] = releaseTimes[0]
        for i in range(1 , len(releaseTimes)):
            arr[i] = releaseTimes[i] - releaseTimes[i-1]
        maximum = max(arr)
        ans = [v for k , v in zip(arr , keysPressed) if k == maximum]
        ans = sorted(ans)
        return ans[-1]
