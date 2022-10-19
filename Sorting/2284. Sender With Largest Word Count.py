class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        senderMessage = collections.defaultdict(int)

        for message , sender in zip(messages , senders):
            for m in message.split(" "):
                senderMessage[sender] += 1
        senderMessage = sorted(senderMessage.items()  , key= lambda x : (x[1] , x[0]))
        ans = senderMessage[-1][0]
        return ans
