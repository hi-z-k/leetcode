class Solution:
    def minOperations(self, logs: list[str]) -> int:
        operations = 0
        for action in logs:
            if action == "../":
                if operations:
                    operations -= 1
                continue
            elif action == "./":
                continue
            else:
                operations += 1
        return operations