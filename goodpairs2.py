#TODO: Find the total number of good pairs.
#A Good pair is a pair of numbers that equal each other but the index of the second number is higher than the first
#create a dictionary with keys of the number being evaluated, and the value the number of times the number has been seen so far
#If it's been seen the value will be incremented by 1
#once the whole list is ran through the total will be the total number of times two numbers have been found in the list 
#with a higher index for the second. 
#we will create a variable called prev which will be the value at the key of the number we're evaluating
#if we don't see it in there it'll just return 0
#if we do so it we'll add prev to the total
#after that, we'll add 1 to the value at the key of the num we're looking at


class Solution:
    def __init__(self, nums):
        """
        nums type: int - [List]
        rtype: int
        """

    def goodPairs(nums):
        
        total = 0
        counts = {}

        for i in range(0, len(nums)):
            prev = counts.get(nums[i], 0)
            total += prev
            counts[nums[i]] = prev + 1

        return total
    



nums = [1, 2, 3, 1, 2, 1]  #should return 3

sol = Solution

print(sol.goodPairs(nums))