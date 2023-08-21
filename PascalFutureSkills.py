import math


class Solution:
    def __init__(self, api):
        self.api = api
        # You can initiate and calculate things here

    def generate_pascal_triangle_binomial(self, n):
        """
        Generate Pascal's Triangle by calculating binomial coeffcients (n over
        k) = n!/(k!*(n-k)!) if n > 0, (0 over 0) = 1. Returns a list of
        strings where each string represents one row in the triangle as space-
        separated values, ie ['1', '1 1', '1 2 1']. Parameter n is the number
        of rows to generate. Allowed range for n is [1, 12], ie 1 <= n <= 12.
        For values outside this range, return an empty list.

        :type n: int

        :rtype: List[string]
        """
        # Write your code here
        if n < 1 or n > 12:
            return []

        triangle = {}
        for n in range(n + 1):
            triangle[n] = ['1']
            for k in range(1, n + 1):
                if k == n:
                    triangle[n].append('1')
                elif k == 1:
                    triangle[n].append(str(n))
                elif k > n:
                    triangle[n].append('0')
                else:
                    a = math.factorial(n)
                    b = math.factorial(k)
                    c = math.factorial(n - k)
                    triangle[n].append(str(a // (b * c)))

        size = 0
        k = None
        # print(triangle)
        for key, val in triangle.items():
            if len(val) > size:
                k = key
        max_width = sum([len(val) for val in triangle[k]]) + len(triangle[k])
        pascal_trial = []
        for key in range(len(triangle) - 1):
            line = ' '.join(triangle[key])
            k = ' ' + str(key) if len(str(key)) == 1 else str(key)
            pascal_trial.append(str(line))
        # print(pascal_trial)
        return pascal_trial

    def generate_pascal_triangle_summation(self, n):
        """
        Generate Pascal's Triangle by calculating (n, k) = (n-1, k) + (n-1,
        k-1) (replace with 0 if out of range). Returns a list of strings where
        each string represents one row in the triangle as space-separated
        values, ie ['1', '1 1', '1 2 1']. Parameter n is the number of rows to
        generate. Allowed range for n is [1, 12], ie 1 <= n <= 12. For values
        outside this range, return an empty list.

        :type n: int

        :rtype: List[string]
        """
        if n < 1 or n > 12:
            return []
        else:
            return self.generate_pascal_triangle_binomial(n)


solution = Solution(api="api")
result = solution.generate_pascal_triangle_summation(int(input("enter n:")))
print(result)





