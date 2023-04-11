class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        m , p , g = 0 , 0 , 0
        N = len(travel)
        d = dict()
        # get the last index of M , G , P
        for i in range(len(garbage)):
            if "M" in garbage[i]:
                d["M"] = i
            if "P" in garbage[i]:
                d["P"] = i
            if "G" in garbage[i]:
                d["G"] = i
        # initialize a prefix array 
        prefixSum = [0] * (N) 
        prefixSum[0] = 0
        for i in range( N):
            prefixSum[i] = prefixSum[i - 1] + travel[i]      
        for i in range(len(garbage)):
            for j in range(len(garbage[i])):
                if garbage[i][j] == "M":
                    m += 1
                elif garbage[i][j] == "P":
                    p += 1
                elif garbage[i][j] == "G":
                    g += 1
        # add the time it takes to travel to the last occurence of M , P , g
        if ("M" in d.keys() and d["M"] > 0 ):
            m += prefixSum[(d["M"] - 1)]
        if  ("P" in d.keys() and d["P"] > 0):
            p += prefixSum[(d["P"] - 1)]
        if  ("G" in d.keys() and d["G"] > 0) :
            g += prefixSum[(d["G"] - 1)]
       
        return m + p + g
