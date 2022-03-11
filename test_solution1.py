import unittest
import solution1

class TestSolution1(unittest.TestCase):

    def test_check_size_whole_string(self):
        str='abcabcabcabcabc'
        substr='abcabcabcabcabc'
        result = solution1.check_substring(str,substr)
        self.assertTrue(result)


    def test_check_size_half_string(self):
        str='abcdabcdabcdabcd'
        substr='abcdabcd'
        result = solution1.check_substring(str,substr)
        self.assertTrue(result)    

    def test_check_size_quarter_string(self):
        str='abcdabcdabcdabcd'
        substr='abcd'
        result = solution1.check_substring(str,substr)
        self.assertTrue(result)      

    def test_check_size_eighth_string(self):
        str='abcdabcdabcdabcd'
        substr='ab'
        result = solution1.check_substring(str,substr)
        self.assertFalse(result)   


    def test_solution_should_be_4(self):
        str='abcdabcdabcdabcd'
        result = solution1.solution(str)
        self.assertEqual(4,result)\

    def test_solution_should_be_1(self):
        str='abcabcabcabcabca'
        result = solution1.solution(str)
        self.assertEqual(1,result)            

    def test_solution_should_be_3(self):
        str='abcabcabcabcabc'
        result = solution1.solution(str)
        self.assertEqual(5,result)   