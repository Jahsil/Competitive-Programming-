class Solution:
    def dayOfYear(self, date: str) -> int:
        year = int(date[0:4])
        if year % 4 != 0 :
            # leap year
            months = [31,28,31,30,31,30,31,31,30,31,30,31]
        elif year == 1900:
            months = [31,28,31,30,31,30,31,31,30,31,30,31]
        else:
            months = [31,29,31,30,31,30,31,31,30,31,30,31]
        prefixsum = [0] * len(months)
        prefixsum[0] = months[0]
        for i in range(1 , len(months)):
            prefixsum[i] = prefixsum[i-1] + months[i]
        currentdate = int(date[-2] + date[-1])
        currentmonth = int(date[-5] + date[-4])
        return prefixsum[currentmonth - 2] + currentdate if currentmonth != 1 else currentdate
        
        
        
        
