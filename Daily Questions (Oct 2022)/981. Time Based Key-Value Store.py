class TimeMap:

    def __init__(self):
        self.d = defaultdict(deque)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].appendleft((-timestamp , value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        
        index = bisect.bisect_left(self.d[key] , (-timestamp , ''))
        if index >= len(self.d[key]):
            return ""
        return self.d[key][index][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
