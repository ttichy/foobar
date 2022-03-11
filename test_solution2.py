import unittest
import solution2

class TestSolution1(unittest.TestCase):

    def test_20220_should_return_8(self):
        array=[2, 0, 2, 2, 0]
        result = solution2.solution(array)

        self.assertEqual("8",result)


    def test_should_be_30(self):
        array=[2,-3,1,0,-5]
        result = solution2.solution(array)

        self.assertEqual("30",result)


    def test_with_single_panel(self):
        result=solution2.solution([4])
        self.assertEqual("4",result)

    def test_with_empty_panel(self):
        result=solution2.solution([])
        self.assertEqual("0",result)      

    def test_with_one_zero_panel(self):
        result=solution2.solution([0])
        self.assertEqual("0",result)            

    def test_one_negative_with_zeros(self):
        result = solution2.solution([-3,0,0,0,0,0])
        self.assertEqual("0",result)

    def test_with_all_zeroes_panel(self):
        result=solution2.solution([0,0,0,0,0,0])
        self.assertEqual("0",result)           


    def test_with_negatives(self):
        result=solution2.solution([0,-2,-1,0,-1,0,-2,-1])
        self.assertEqual("4",result)         

    def test_with_3_negatives(self):
        result=solution2.solution([-2, -3, 4, -5])
        self.assertEqual("60",result)          

    def test_with_only_1_negatives(self):
        result=solution2.solution([-2])
        self.assertEqual("-2",result)          


    def test_with_zeroes_and_1_negative(self):
        result=solution2.solution([0,0,0,0,-2])
        self.assertEqual("0",result)         


    def test_with_large_output(self):
        result=solution2.solution(range(1,51))
        self.assertEqual("30414093201713378043612608166064768844377641568960512000000000000",result)          