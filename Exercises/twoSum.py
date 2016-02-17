def twoSum(nums, target):

    for i in range(len(nums)):

        for j in range(i+1, len(nums)):

            if nums[i]+nums[j] == target and nums[i] != nums[j]:

                return [i, j]


