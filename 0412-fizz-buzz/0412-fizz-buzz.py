class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        numList = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                numList.append("FizzBuzz")
            elif i % 3 == 0:
                numList.append("Fizz")
            elif i % 5 == 0:
                numList.append("Buzz")
            else:
                numList.append(str(i))
        return numList
        