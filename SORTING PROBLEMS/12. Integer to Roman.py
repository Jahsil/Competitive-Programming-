roman = {
 1     :    'I',
 5     :'V'  ,
  10    : 'X' ,
 50    :'L' ,
 100   :'C',
 500   :'D',
1000  :'M',
    4 : 'IV',
    9 : 'IX',
    40 : 'XL',
    90 : "XC",
    400: "CD",
    900:"CM"
}
print(roman)
num = '1884'
print(str(num))
arr = []
j = 1
for i in range(len(num)-1 , -1 , -1):
    arr.append(int(num[i]) * j)
    j *= 10

arr = sorted(arr , reverse= True)
print(arr)
ans = ""
for i in range(len(arr)):
    if arr[i] in roman:
        ans += roman[arr[i]]
