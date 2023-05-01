pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
def validateStackSequences( pushed, popped):
    newPushed  = []
    j = 0
    for i in pushed:
        newPushed.append(i)
        while(newPushed is not None and j < len(popped) and newPushed[-1] == popped[j]):
            newPushed.pop()
            j+=1
    return j == len(popped)




print(validateStackSequences(pushed , popped))
