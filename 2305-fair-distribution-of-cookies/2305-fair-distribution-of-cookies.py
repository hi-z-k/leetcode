class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse=True)
        minUnfairness = sum(cookies)
        children = [0]*k

        def backtrack(i):
            nonlocal minUnfairness
            if i == len(cookies):
                minUnfairness = min(minUnfairness, max(children))
                return
            if max(children) >= minUnfairness:
                return
            for m in range(k):
                children[m] += cookies[i]
                backtrack(i+1)
                children[m] -= cookies[i]
        backtrack(0)
        return minUnfairness