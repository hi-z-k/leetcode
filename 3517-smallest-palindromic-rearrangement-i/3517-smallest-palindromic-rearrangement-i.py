class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # startegy is put it into a counter and find the min
        # after that append freq//2 in the string if freq freq//2 + 1
        count = Counter(s)
        middle = ""
        half = []
        for i in range(len(count)):
            letter = min(count.keys())
            freq = count[letter]
            final_freq = freq // 2
            if freq % 2 != 0:
                middle = letter
            half.append(letter * final_freq)
            del count[letter]
        output = "".join(half) + middle + "".join(half[::-1])
        return output
