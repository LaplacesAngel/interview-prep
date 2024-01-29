def twoSum(nums, target):

    seen = {}  #empty seen dictionary

    for i, num in enumerate(nums): #iterate through the array of possible numbers

        remainder = target - num  #find the difference between the target and our current number

        #start evaluating nums to see if they're already in the list
        
        if remainder in seen:               #evals if the difference between the target and the current number is already in the list, when it gets to 1, two will already be in the list, so it will return the index at 2 and the current index
            return [seen[remainder], i]     #works because if the remainder is in there, a number that adds up to itself to equal the target is in the list, we need that numbers index and the current ones
        
        else:
            seen[num] = i  #adds the current number and current index to the dictionary as a key value pair







print(twoSum([2, 3, 1], 3))