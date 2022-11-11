class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        new=[]
        for i in range(1,n+1):
            if i % 15==0:
                new.append('FizzBuzz')
            elif i%3==0:
                new.append("Fizz")
            elif i%5==0:
                new.append('Buzz')
            else:
                new.append(str(i))

        return new