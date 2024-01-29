def twoSum(nums, target):

    seen = {}

    #make a dictionary of numbers you've seen so far with the num as the key and the i as the value

    for i, num in enumerate(nums):
        remaining = target - num  #first time = 3 -2 = 1. 
                                  #Remaining is 1, remaining represents the difference betweent the target and the current number.
                                  #if it ever hits we know we're done because we'll have a number in our list that is the difference the target and our current num, so we need to return the index of our current num and the index of remaining
                                  #second time i is 1, num is 3, remaining = 3 - 3 == 0
        print(f"For our number {num} the remaining is: {remaining} because target is {target} and {target} - {num} = {remaining} \n")

        if remaining in seen:    #remaining will not be in seen b/c it's empty
            print(f"seen[{remaining}] aka seen at remaining of {remaining} is index: {seen[remaining]}. Our current index is {i}")
            return [seen[remaining], i] #skip first time
        
        else:
            seen[num] = i #will add 1 to the dictionary with an index of 0, dict will look like {2, 0}
            print(f"Seen dictionary is now {seen} because our number {num} was not already in the dictionary and thus was added along with our current index: {i} \n")


print(twoSum([2, 3, 1], 3))