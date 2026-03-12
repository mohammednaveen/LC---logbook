class Solution(object):
    def numberGame(self, nums):
        length = len(nums)
        arr = [0] * length
        for i in range(length):
            min_idx = i
            for j in range(i+1, length):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            if i % 2 == 0:
                arr[i+1] = nums[min_idx]
            else:
                arr[i-1] = nums[min_idx]
            nums[min_idx] = nums[i]
        return arr

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        