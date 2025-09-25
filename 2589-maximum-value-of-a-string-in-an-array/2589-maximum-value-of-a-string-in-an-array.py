class Solution:
    def numeric(self,alphaNumString:str) -> int:
        try:
            return int(alphaNumString)
        except Exception:
            return len(alphaNumString)
    def maximumValue(self, strs: List[str]) -> int:
        maximum = float("-inf")
        for s in strs:
            maximum = max(self.numeric(s),maximum)
        return maximum
        