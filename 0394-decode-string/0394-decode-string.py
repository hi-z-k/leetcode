class Solution:
    def decodeString(self, s: str) -> str:
        nums = []
        letters = []
        num = 0
        output = ""
        
        for l in s:
            if l == "[":
                nums.append(num)
                letters.append(output)
                num = 0
                output = ""
            elif l == "]":
                n = nums.pop()
                prev_str = letters.pop()
                output = prev_str + (n * output)
            else:
                if l.isdigit():
                    num = num * 10 + int(l)
                else:
                    output += l
                    
        return output