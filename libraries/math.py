class Math:
    
    def gcd(self,a, b):
        """
        Calculate the greatest common factor of two numbers using Euclid's algorithm.
        """
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)
    
    def least_common_multiple(self,numbers):
        """
        Find the least common multiple of a list of numbers.
        """
        result = 1
        for number in numbers:
            result = (result * number) // self.gcd(result, number)

        return result