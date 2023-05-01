import collections

messages = ["How is leetcode for everyone","Leetcode is useful for practice"]
senders = ["Bob","Charlie"]

senderMessage = collections.defaultdict(int)

for message , sender in zip(messages , senders):
    for m in message.split(" "):
        senderMessage[sender] += 1
senderMessage = sorted(senderMessage.items()  , key= lambda x : (x[1] , x[0]))
ans = senderMessage[-1][0]
print(ans)