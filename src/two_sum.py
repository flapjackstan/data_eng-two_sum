class Solution:
    def two_sum_dictionary(self, nums: list, target: int):
        print(f'list:{nums}', f'target: {target}')
        
        dictionary = {}
        
        for index, item in enumerate(nums):
            if item < target:
                dictionary[item] = index

        for item in dictionary:
            
            diff = target - item

            if diff in dictionary:
                return [dictionary[item], dictionary[diff]]


    def two_sum_list(self, nums: list, target: int) -> list:
        print(f'list:{nums}', f'target: {target}')
        
        for index1, item1 in enumerate(nums):
            
            for index2, item2 in enumerate(nums):

                if item1 + item2 == target:
                    return [index1, index2]
                    

    def two_sum_elim_list(self, nums: list, target: int) -> list:
        print(f'list:{nums}', f'target: {target}')
        
        for index1, item1 in enumerate(nums):
            
            for index2, item2 in enumerate(nums[ index1 + 1 : ]):

                if item1 + item2 == target:
                    return [index1, index1 + index2 + 1]