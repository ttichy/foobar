import unittest
import solution5
from fractions import Fraction

class TestSolution5(unittest.TestCase):

    def test_state_prob_1(self):
        result = solution5.state_prob([0,1,0,0,0,1],1)
        self.assertEqual(result[0],0)
        self.assertEqual(result[1],Fraction(1,2))
        self.assertEqual(result[2],0)
        self.assertEqual(result[3],0)
        self.assertEqual(result[4],0)
        self.assertEqual(result[5],Fraction(1,2))



    def test_state_prob_2(self):
        result = solution5.state_prob([4,0,0,3,2,0],Fraction(1,2))
        self.assertEqual(result[0],Fraction(2,9))
        self.assertEqual(result[1],0)
        self.assertEqual(result[2],0)
        self.assertEqual(result[3],Fraction(3,18))
        self.assertEqual(result[4],Fraction(1,9))
        self.assertEqual(result[5],0)        

        