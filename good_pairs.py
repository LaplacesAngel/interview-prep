#TODO: Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# all about the indices here, if the index of a number is less than the index of another number in a list, 
# and the numbers are the same, put the pair of the indices in an arrary

class Solution:
    def numIdenticalPairs(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """

        #number and index in list
        goodpairs = []

        for i, num in enumerate(nums):
            for j, numsagain in enumerate(nums):
                if num == numsagain and i < j:
                    pairs = (i, j)
                    goodpairs.append(pairs)

        return len(goodpairs)
    

    #with a dict:
    def numIdenticalPairsDict(self, nums):

        total = 0
        counts = {}

        for i, num in enumerate(nums):
            prev = counts.get(num, 0)
            print(f"counts is {counts} at the beginning of turn {i}")
            print(f"Num is {num} and counts.get({num}) is {prev} on turn {i}")
            total = total + prev
            print(f"Total is {total} on turn {i}")
            counts[num] = prev + 1
            print(f"counts is {counts} at the end of turn {i}")

        return total



nums = [1,2,3,1,1,3]

s1 = Solution()
print(f"Nested loop solution: {s1.numIdenticalPairs(nums)}")
print(f"Dictionary solution: {s1.numIdenticalPairsDict(nums)}")

