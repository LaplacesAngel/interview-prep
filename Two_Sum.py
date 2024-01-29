class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        pairs = {}
        solution = []
        solution_indices = []

        for i, num in enumerate(nums):
            compliment = target - num
            if num in pairs:
                return [pairs[num], i]
            pairs[num] = 1

            return pairs





        prac





        #     compliment = target - num
        #     if compliment in pairs:
        #         return [pairs[compliment], i]
        #     pairs[num] = i

        # print(pairs)


        #     for y in nums:
        #         if y == target -x:
        #             solution.append(x)
        #             print(solution)
        #             solution.append(y)
        #             print(solution)
        
        # solution_nums =  list(set(solution))

        # print(solution_nums)

        # for x in solution_nums:
        #     solution_indices.append(nums.index(x))

        # return solution_indices    

        # solution_indices.append(nums.index(solution_nums[0]))
        # solution_indices.append(nums.index(solution_nums[1]))
    

    
test1 = Solution().twoSum([3,2,4], 6)

print(test1)