class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j = 0, len(people)-1
        numBoat = 0
        while(i<=j):
            print(people[i],people[j],people[i] + people[j])
            if people[i] + people[j] <= limit or i == j:
                i += 1
                j -= 1
            elif people[j] <= limit:
                j -= 1
            else:
                i += 1
            numBoat += 1
        return numBoat