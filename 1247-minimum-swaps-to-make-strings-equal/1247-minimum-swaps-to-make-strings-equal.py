class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = 0
        yx = 0
        for i in range(len(s1)):
            l1 = s1[i]
            l2 = s2[i]
            if l1 == l2:
                continue

            if l1 == "x" and l2 =="y":
                xy += 1
            elif l1 == "y" and l2 =="x":
                yx += 1
       
        sum = xy + yx
        if sum % 2 != 0:
            return -1
        result = int(xy//2 + yx//2)
        if xy % 2 != 0:
            result += 2
        return result
        