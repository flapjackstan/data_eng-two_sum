'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

'''

import pytest
from src.two_sum import Solution

def main():

    # exit_code = pytest.main(["tests/","-s"])  # noqa: E501

    # if exit_code > 0:
    #         print("See Above For Pytest Error Output!")

    # else:
    #     print("All Tests Passed!")

    solution_obj = Solution()

    print(solution_obj.two_sum_list([3,4,8,9],12))

if __name__ == '__main__':
    main()