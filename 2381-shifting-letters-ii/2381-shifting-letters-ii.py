class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        length = len(s)
        shift_update = [0]*(length+1)
        for start,end,direction in shifts:
            if direction == 0:
                direction = -1
            shift_update[start] += direction
            if end + 1 < length:
                shift_update[end+1] -= direction
        for i in range(1,length+1):
            shift_update[i] += shift_update[i-1]
        output = []
        for i,shift in enumerate(shift_update):
            if i < length:
                idx = (ord(s[i])-97) 
                idx += shift
                ascii_letter = (idx % 26) + 97
                output.append(chr(ascii_letter))
        return "".join(output)
