arr = []
def reverseString(word):
    s = ""
    length = len(word)
    #arr = []
    j = length-1
    for i in range(0, length):
        if j >= 0 :
            arr.append(word[j])
            j-=1
    return arr
def displayString():
    word = ""
    for i in arr:
        word += i
    print(word)
word = "hello world"
reverseString(word)
displayString()
