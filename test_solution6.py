import unittest
import solution6
from fractions import Fraction

class TestSolution6(unittest.TestCase):

    def test_pair_up_with_4_7(self):
        (pairs, leftover,) = solution6.pair_up(4,7)
        self.assertEqual(pairs,4)
        self.assertEqual(leftover,3)


    def test_pair_up_with_2_1(self):
        (pairs, leftover,) = solution6.pair_up(2,1)
        self.assertEqual(pairs,1)
        self.assertEqual(leftover,1)

    def test_solution_with_2_4_should_be_impossible(self):
        result = solution6.solution('2','4')

        self.assertEqual(result,'impossible')

    def test_solution_with_3_3_should_be_impossible(self):
        result = solution6.solution('3','3')

        self.assertEqual(result,'impossible')        


    def test_solution_with_4_7_should_be_4(self):
        result = solution6.solution('4','7')

        self.assertEqual(result,'4') 

    def test_solution_with_2_1_should_be_1(self):
        result = solution6.solution('2','1')

        self.assertEqual(result,'1')         

    def test_solution_with_4_6_should_be_impossible(self):
        result = solution6.solution('4','6')

        self.assertEqual(result,'impossible')                

    def test_solution_with_5_9_should_be_5(self):
        result = solution6.solution('5','9')

        self.assertEqual(result,'5')      


    def test_solution_with_5_6_should_be_5(self):
        result = solution6.solution('5','6')

        self.assertEqual(result,'5')         

    def test_solution_with_5_7_should_be_4(self):
        result = solution6.solution('5','7')

        self.assertEqual(result,'4')       

    def test_solution_with_6_9_should_be_impossible(self):
        result = solution6.solution('6','9')

        self.assertEqual(result,'impossible')                     

    def test_solution_with_17_20_should_be_8(self):
        result = solution6.solution('17','20')

        self.assertEqual(result,'8')             

    def test_shortcut(self):
        (short,left) = solution6.shortcut(17,3)

        self.assertEqual(short,5)
        self.assertEqual(left,2)

    def test_solution_with_18_21(self):
        result = solution6.solution('18','21')
        self.assertEqual(result,'impossible')


    def test_solution_with_large_numbers(self):
        result = solution6.solution('21205',str(21205+9031))

          