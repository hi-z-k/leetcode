class Solution:
    def repeatedCharacter(self, s: str) -> str:
        appeared = set()
        for l in s:
            if l in appeared:
                return l
            appeared.add(l)
        return ""