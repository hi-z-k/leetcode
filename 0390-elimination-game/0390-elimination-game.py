class Solution:
    def lastRemaining(self, n: int) -> int:
        def remove(m):
            if m == 1:
                return 1
            return 2 * (m // 2 + 1 - remove(m // 2))
        return remove(n)