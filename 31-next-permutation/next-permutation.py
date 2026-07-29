class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)
        ind = -1

        
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                ind = i
                break

       
        if ind == -1:
            nums.reverse()
            return

        for i in range(n - 1, ind, -1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
                break

        left, right = ind + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1