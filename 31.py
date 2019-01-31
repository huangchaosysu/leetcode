class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return

        flag = False
        i = len(nums) - 1
        while i > 0:
            if nums[i-1] >= nums[i]:
                i -= 1
            else:
                i -= 1
                flag = True
                break

        if i == 0 and not flag:
            j = len(nums) - 1
            while j > i:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            return

        m = len(nums) - 1
        while m > i:
            if nums[m] > nums[i]:
                nums[m], nums[i] = nums[i], nums[m]
                break
            m -= 1
        z, x = i+1, len(nums) - 1
        while x > z:
            nums[z], nums[x] = nums[x], nums[z]
            z += 1
            x -= 1

        # print(nums)
        return
