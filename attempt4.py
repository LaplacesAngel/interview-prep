def twoSum(nums, target):

    seen = {}

    for i, num in enumerate(nums):
        remainder = target - num

        if remainder in seen:
            return [seen[remainder], i]
        
        else:
            seen[num] = i