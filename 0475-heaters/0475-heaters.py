class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        max_distance = 0
        heaters.sort()
        for house in houses:
            left = 0
            right = len(heaters)-1
            while left <= right:
                middle = left + (right-left)//2
                if heaters[middle] < house:
                    left = middle + 1
                else:
                    right = middle - 1

            heater1 = float("-inf")
            heater2 = float("-inf")
            if right >= 0:
                heater1 = heaters[right]
            if left < len(heaters):
                heater2 = heaters[left]
            if house == heater1:
                continue
            distance = min(abs(house-heater1),abs(house-heater2))
            max_distance = max(distance,max_distance)
        return max_distance