import pytest
from src.two_sum import Solution

@pytest.fixture(scope='module')
def solution_obj():
    print("This happened once")
    return Solution()
