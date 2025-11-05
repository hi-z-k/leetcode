class Solution:
    @staticmethod
    def squareDistanceToOrigin(point:List[int])->int:
        x1,y1 = point[0],point[1]
        return ((x1)**2 + (y1)**2)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = Solution.squareDistanceToOrigin
        points.sort(key=distance)
        return points[:k]