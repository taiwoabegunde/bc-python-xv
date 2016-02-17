def max_num(nums):
    max = 0
    list_length = range(len(nums))
    for i in list_length:
        if max < nums[i]:
            max = nums[i]
    return max
        
print (max_num([2,1,7,5,12,3,45,667,1123]))