class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        extract = lambda row: row[k]
        score.sort(key=extract)
        score.reverse()
        return score