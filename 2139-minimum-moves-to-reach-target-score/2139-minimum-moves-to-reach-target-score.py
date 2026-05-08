class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        end = target
        double = maxDoubles
        count = 0
        while target > 1:
            if not double:
                count += (target - 1)
                break
            if target % 2 == 0 and double:
                target //= 2
                double -= 1
            else:
                target -= 1
            count += 1
        return count