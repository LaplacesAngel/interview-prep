#TODO: Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# all about the indices here, if the index of a number is less than the index of another number in a list, 
# and the numbers are the same, put the pair of the indices in an arrary

def numIdenticalPairs(nums):

    """
    :type nums: List[int]
    :rtype: int
    """

    #number and index in list
    dict = {
        1:0,
        2:1,
        3:2,
        1:3,
        1:4,
        3:5
    }

    goodpairs = []

    

    for i in range(0, len(nums)):
        for key, value in dict.items():
            if nums[i] == key and i < value:
                print(f"On round {i}: \n nums[i] is {nums[i]} \n key is {key} \n value is {value}")
                tuple = (i, value)
                print(tuple)
                goodpairs.append(tuple)

   

    return len(goodpairs)


nums = [1,2,3,1,1,3]

print(numIdenticalPairs(nums))