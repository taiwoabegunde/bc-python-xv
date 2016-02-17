def max_min(nums):
  count = nums[0]
  for i in num:
    if i < count:
      count = i
      result = []
      result = result.append(count)
    elif i > count:
      count = i
      result = result.append(count)
    else:
      return result