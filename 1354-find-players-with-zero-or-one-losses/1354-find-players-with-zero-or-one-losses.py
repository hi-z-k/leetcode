from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss = defaultdict(int)
        for match in matches:
            winner = match[0]
            looser = match[1]
            loss[looser] += 1
            if winner not in loss:
                loss[winner] = 0
        winner = []
        looser = []
        for player in loss:
            if loss[player] == 0:
                winner.append(player)
            elif loss[player] == 1:
                looser.append(player)
        winner.sort()
        looser.sort()
        return [winner,looser]