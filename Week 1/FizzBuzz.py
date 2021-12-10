class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        numbers = []
        for num in range (1, n + 1):
            if num % 3 == 0 and num % 5 == 0 :
                numbers.append("FizzBuzz")
            elif num % 3 == 0 :
                numbers.append("Fizz")
            elif num % 5 == 0 :
                numbers.append("Buzz")
            else : 
                numbers.append(str(num))
        return numbers
        
