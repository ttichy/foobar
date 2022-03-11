import time
import unittest
import solution4

class TestSolution3(unittest.TestCase):

    def test_123456_should_be_123_126_136(self):
        result = solution4.solution([1, 2, 3, 4, 5, 6])
        result2 = solution4.solution2([1, 2, 3, 4, 5, 6])
        self.assertEqual(result,3)
        self.assertEqual(result,result2)


    def test_111_should_be_111(self):
        result = solution4.solution([1,1,1])
        result2 = solution4.solution2([1,1,1])
        self.assertEqual(result,1)        
        self.assertEqual(result,result2)

    def test_123_should_be_none(self):
        result = solution4.solution([1,2,3])
        result2 = solution4.solution2([1,2,3])
        self.assertEqual(result,0)
        self.assertEqual(result,result2)

    def test_with_multiples(self):
        result = solution4.solution([1,1,1,1])
        result2 = solution4.solution2([1,1,1,1])
        self.assertEqual(result,4)
        self.assertEqual(result,result2)

    def test_length_2_should_be_0(self):
        result = solution4.solution([1,1])
        result2 = solution4.solution2([1,1])
        self.assertEqual(result,0)        
        self.assertEqual(result,result2)

    def test_654321_should_be_0(self):
        result = solution4.solution([6,5,4,3,2,1])
        result2 = solution4.solution2([6,5,4,3,2,1])
        self.assertEqual(result,0)
        self.assertEqual(result,result2)

    def test_124_should_be_1(self):
        result = solution4.solution([1,2,4])
        result2 = solution4.solution2([1,2,4])
        self.assertEqual(result,1)
        self.assertEqual(result,result2)


    def test_248_should_be_1(self):
        list=[1,2,4,8,2,55,4,8,2,4,8,1]
        result = solution4.solution(list)
        result2 = solution4.solution2(list)
        self.assertEqual(result,result2)
        # self.assertEqual(result,10)

    def test_12345612_should_be_7(self):
        list=[1,2,3,4,5,6,12]
        result = solution4.solution(list)
        result2 = solution4.solution2(list)
        self.assertEqual(result,result2)