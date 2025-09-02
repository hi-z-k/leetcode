class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        length = len(cardPoints)
        left = length - k
        right = length - 1
        currentSum = sum(cardPoints[left:])
        maxSum = currentSum
        while(left < length):
            currentSum -= cardPoints[left]
            left += 1
            right = ((left + k - 1) % length)
            currentSum += cardPoints[right]
            maxSum = max(maxSum, currentSum)
        return maxSum