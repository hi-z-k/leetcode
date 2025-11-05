class Solution:
    @staticmethod
    def squareDistanceToOrigin(point:List[int])->int:
        x1,y1 = point[0],point[1]
        return ((x1)**2 + (y1)**2)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = Solution.squareDistanceToOrigin
        lengthHash = {}
        for point in points:
            d = distance(point)
            if d in lengthHash:
                lengthHash[d].append(point)
            else:
                lengthHash[d] = [point]
        dist = list(lengthHash.keys())
        dist.sort()
        output = []
        length = min(k,len(dist))
        for i in range(length):
            output.extend(lengthHash[dist[i]])
        return output[:k]