def twoSum(nums, target):

    seen = {}

    for i in range(0, len(nums)):
        remainder = target - nums[i]

        if remainder in seen:
            return [seen[remainder], i]
        
        else:
            seen[nums[i]] = i


#kind of like this one better because I have to keep better mental track of each iteration to tell what's going on each time 
#and range is maybe more common than enumerate in other languages