class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = Counter(ransomNote)
        newspaper = Counter(magazine)
        return ransom <= newspaper