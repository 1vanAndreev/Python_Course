def find_and_replace_missing(nums):
    missing_index = nums.index(None)
    sum_without_missing = sum(num for num in nums if num is not None)
    amount = len(nums)
    nums[missing_index] = sum_without_missing / amount
    return nums

numbers = [1, 2, None, 4, 5]
result = find_and_replace_missing(numbers)
print(result)
