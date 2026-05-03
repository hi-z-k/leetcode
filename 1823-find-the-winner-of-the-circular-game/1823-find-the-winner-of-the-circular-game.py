class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = list(range(1,n+1))
        start = 0
        def play():
            nonlocal start
            loser = (start+k-1) % len(players)
            start = loser
            players.pop(loser)
        while len(players) > 1:
            play()
        return players[0]
