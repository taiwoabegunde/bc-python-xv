def twoSum(nums, target):
    index_dict = {}
    list_sum = range(len(nums))
    for i in list_sum:
        both_diff = i - target
        if both_diff not in index_dict:
            index_dict[nums[i]] = i
        else:
            return [index_dict[both_diff], i]   