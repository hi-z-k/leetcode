class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        frequency = [[] for _ in range(len(s)+1)]
        for letter,freq in count.items():
            frequency[freq].append(letter*freq)
        output = []
        for i in range(len(frequency)-1, -1, -1):
            output.extend(frequency[i])
        return "".join(output)