'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

'''

import pytest

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


    def two_sum_list(self, nums: list[int], target: int) -> list[int]:
        print(f'list:{nums}', f'target: {target}')
        
        for index1, item1 in enumerate(nums):
            
            for index2, item2 in enumerate(nums):

                if item1 + item2 == target:
                    return [index1, index2]
                    

    def two_sum_elim_list(self, nums: list[int], target: int) -> list[int]:
        print(f'list:{nums}', f'target: {target}')
        
        for index1, item1 in enumerate(nums):
            
            for index2, item2 in enumerate(nums[ index1 + 1 : ]):

                if item1 + item2 == target:
                    return [index1, index1 + index2 + 1]

def main():

    exit_code = pytest.main(["tests/","-s"])  # noqa: E501

    if exit_code > 0:
            print("See Above For Pytest Error Output!")

    else:
        print("All Tests Passed!")

if __name__ == '__main__':
    main()