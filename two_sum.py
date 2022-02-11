'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

'''

class Solution:
    def two_sum_dictionary(self, nums: list[int], target: int) -> list[int]:
        print(f'list:{nums}', f'target: {target}')
        
        dictionary = {}
        
        for index, item in enumerate(nums):
            if item < target:
                dictionary[item] = index

        for item in dictionary:
            
            diff = target - item

            if diff in dictionary:
                return [dictionary[item], dictionary[diff]]

def main():
    solution = Solution()

    two_sum = solution.two_sum_dictionary([4,7,9,10,15,22,24,25,36], 35)
    print('solution:' + str(two_sum))

if __name__ == '__main__':
    main()