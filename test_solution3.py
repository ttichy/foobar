import unittest
import solution3

class TestSolution3(unittest.TestCase):

    def test_4_30_50_should_be_12_1(self):
        array=[4,30,50]
        result = solution3.solution(array)

        self.assertEqual([12,1],result)

    def test_4_17_50_should_be_m1_m1(self):
        array=[4,17,50]
        result = solution3.solution(array)

        self.assertEqual([-1,-1],result)


    def test_4_28_should_be_16_1(self):
        array=[4,28]
        result = solution3.solution(array)

        self.assertEqual([16,1],result)



    def test_0_0_should_be_m1_m1(self):
        array=[0,0]
        result = solution3.solution(array)

        self.assertEqual([-1,-1],result)        

    def test_0_0_0_should_be_m1_m1(self):
        array=[0,0,0]
        result = solution3.solution(array)

        self.assertEqual([-1,-1],result)                

    def test_with_long_list_of_pegs(self):
        array=[4,30,50,80,90,120,140,1500,2000,3000,5000,6000,7000]
        result = solution3.solution(array)

        self.assertEqual([-1,-1],result)            

    def test_with_1_3_4_should_be_m1_m1(self):
        # this has a zero gear!
        array=[1,3,4]
        result = solution3.solution(array)

        self.assertEqual([-1,-1],result)            
    
    
    def test_with_4_valid_pegs_should_work(self):
        # this has a zero gear!
        array=[4,30,50,68]
        result = solution3.solution(array)

        self.assertEqual([16,1],result)            

    def test_with_2_consecutive_pegs_should_work(self):
        # this has a zero gear!
        array=[4,5]
        result = solution3.solution(array)

        self.assertEqual([-1,-1],result)             