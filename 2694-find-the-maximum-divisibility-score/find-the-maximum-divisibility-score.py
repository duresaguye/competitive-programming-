class Solution:
    def maxDivScore(self, nums, divisors):
        max_score = 0
        min_divisor = float('inf')

        for divisor in divisors:
            score = sum(1 for num in nums if num % divisor == 0)

            if score > max_score or (score == max_score and divisor < min_divisor):
                max_score = score
                min_divisor = divisor

        return min_divisor