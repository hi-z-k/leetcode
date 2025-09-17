class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j = 0, len(people)-1
        numBoat = 0
        while(i<=j):
            currentSum = people[i] + people[j] 
            if currentSum <= limit or i == j:
                i += 1
                j -= 1
            elif people[j] <= limit:
                j -= 1
            else:
                i += 1
            numBoat += 1
        return numBoat