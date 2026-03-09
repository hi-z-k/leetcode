class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level = 0
        for directory in logs:
            if directory == "../":
                if level:
                    level -= 1
            elif directory == "./":
                continue
            else:
                level += 1
        return level