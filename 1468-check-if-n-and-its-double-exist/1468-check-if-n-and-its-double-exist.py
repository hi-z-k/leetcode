class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        numsToLookFor = set()
        for integer in arr:
            if integer in numsToLookFor:
                print(integer)
                return True
            if integer % 2 == 0:
                numsToLookFor.add(integer//2)
            numsToLookFor.add(integer*2)
            print(numsToLookFor)
        return False 