class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        response = []
        for servey in responses:
            servey = list(set(servey))
            response.extend(servey)
        count = Counter(response)
        maxCount = max(count.values())
        most_common = [r for r,c in count.items() if c ==  maxCount]
        return min(most_common)