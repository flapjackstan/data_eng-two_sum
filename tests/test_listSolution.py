import pytest

class TestSolution:
    def setup_method(self):
        print("Setup!")
        self.list_1 = [5,8,10,13,15,74,100]
        self.target_1 = 87

    def teardown_method(self):
        print("Teardown!")
        self.list_1 = None
        self.target_1 = None

    def test_listSolution(self, solution_obj):

        print(solution_obj.two_sum_list(self.list_1,self.target_1))

    def test_elimListSolution(self, solution_obj):

        print(solution_obj.two_sum_elim_list(self.list_1,self.target_1))

    def test_dictSolution(self, solution_obj):

        print(solution_obj.two_sum_dictionary(self.list_1,self.target_1))
