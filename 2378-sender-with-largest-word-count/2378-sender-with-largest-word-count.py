class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        wordSent = defaultdict(int)
        for i,msg in enumerate(messages):
            msgData = msg.split()
            sender = senders[i]
            wordSent[sender] += len(msgData)
        maxSender = None
        for sender in wordSent:
            if not maxSender or wordSent[sender] > wordSent[maxSender]:
                maxSender = sender
            elif wordSent[sender] == wordSent[maxSender] and sender > maxSender:
                maxSender = sender
        return maxSender