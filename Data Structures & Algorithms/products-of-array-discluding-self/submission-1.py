class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_mul = 1
        right_mul = 1
        left_product = [0] * n
        right_product = [0] * n

        for i in range(n):
            j = n - i - 1
            left_product[i] = left_mul
            right_product[j] = right_mul
            left_mul = left_mul * nums[i]
            right_mul = right_mul * nums[j]

        result = [0] * n
        for i in range(n):
            result[i] = left_product[i] * right_product[i]
        
        return result