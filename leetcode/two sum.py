import self


class Solution(object):
    def twoSum(self, nums, target):
        self.nums = nums
        self.target = int(target)

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i in range(len(self.nums)):
          for j in range(i + 1, len(self.nums)):
            if self.nums[i] + self.nums[j] == self.target:
                result.append(i)
                result.append(j)


        return list(result)

nums = [2,7,11,15]
target =  9

result = Solution()

print(result.twoSum(nums,target))