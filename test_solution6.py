import unittest
import solution6
import time

class TestSolution6(unittest.TestCase):

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
        result2 = solution6.solution2('17','20')
        self.assertEqual(result2,result)
        self.assertEqual(result,'8')             


    def test_solution_with_18_21(self):
        result = solution6.solution('18','21')
        self.assertEqual(result,'impossible')
        result2 = solution6.solution2('18','21')
        self.assertEqual(result2,result)

    def test_solution_with_11_4_should_be_5(self):
        result = solution6.solution('11','4')
        self.assertEqual(result,'5')
        result2 = solution6.solution2('11','4')
        self.assertEqual(result2,result)


    def test_solution_with_100_1_should_be_99(self):
        result = solution6.solution('100','1')
        result2 = solution6.solution2('100','1')
        self.assertEqual(result2,result)
        self.assertEqual(result,'99')

    def test_solution_with_large_numbers(self):
        result = solution6.solution('21205',str(21205+9031))
        self.assertEqual(result,'29')
        result2 = solution6.solution2('21205',str(21205+9031))
        self.assertEqual(result2,result)


    def test_solution_with_large_numbers3(self):
        result2=solution6.solution2('10000000','9999')
        result = solution6.solution('10000000','9999')
        self.assertEqual(result,result2)

    def test_solution_with_1(self):
        result2 = solution6.solution2('10','1')

    def test_solution_with_large_numbers2(self):
        t0_mine=time.time()
        result = solution6.solution('10^15','12459852189')
        t1_mine = time.time()
        print('mine: {}'.format(t1_mine-t0_mine))

        t0_his = time.time()
        result2 = solution6.solution2('10000000000000000','12459852189')
        t1_his = time.time()
        print('his: {}'.format(t1_his-t0_his))

        self.assertEqual(result2,result)
        self.assertEqual(result,'802761') # not sure about the result here          

    def test_timing(self):
        solution6.timing('1000000','9999')