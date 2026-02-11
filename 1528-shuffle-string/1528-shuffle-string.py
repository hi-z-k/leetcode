class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        output = ["" for i in range(len(s))]
        for i,letter in enumerate(s):
            index = indices[i]
            output[index] = letter
        return "".join(output) 
        