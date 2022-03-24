import unittest
import solution5
from fractions import Fraction

class TestSolution5(unittest.TestCase):

    def test_preprocess_with_case1(self):
        m=[
            [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
            [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
            [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
            [0,0,0,0,0,0],  # s3 is terminal
            [0,0,0,0,0,0],  # s4 is terminal
            [0,0,0,0,0,0],  # s5 is terminal
        ]

        m2 = solution5.copy_matrix(m)

        result = solution5.pre_process_step1(m)
        self.assertEqual(result[0][0],[0,Fraction(1,2),0,0,0,Fraction(1,2)])
        self.assertEqual(result[0][1],[Fraction(4,9), 0,0,Fraction(3,9),Fraction(2,9),0])
        self.assertEqual(result[0][2],[0,0,1,0,0,0])   
        self.assertEqual(result[0][3],[0,0,0, 1,0,0])   
        self.assertEqual(result[0][4],[0,0,0,0, 1,0])   
        self.assertEqual(result[0][5],[0,0,0,0,0,1])   

        self.assertEqual(m,m2)

        # check absorbing states
        self.assertEqual(result[1],[2,3,4,5])


    def test_RQ_extraction(self):
        m=[[0,Fraction(1,2),0,0,0,Fraction(1,2)],
            [Fraction(4,9), 0,0,Fraction(3,9),Fraction(2,9),0],
            [0,0,1,0,0,0],
            [0,0,0, 1,0,0],   
            [0,0,0,0, 1,0],   
            [0,0,0,0,0,1]]

        ab_states =[2,3,4,5]

        (R,Q,states) = solution5.get_R_Q_matrices(m,ab_states)
        self.assertEqual(states,[5,4,3,2,0,1])
        self.assertEqual(Q[0],[Fraction(1,2),0,0,0])
        self.assertEqual(Q[1],[0,Fraction(2,9),Fraction(1,3),0])
        
        self.assertEqual(R[0],[0,Fraction(1,2)])
        self.assertEqual(R[1],[Fraction(4,9),0])


    def test_invert_matrix(self):
        m=[[1,2,3],[3,2,1],[4,2,6]]

        im = solution5.invert_matrix(m)

        self.assertEqual(im[0],[Fraction(-5,12), Fraction(1,4), Fraction(1,6)])
        self.assertEqual(im[1],[Fraction(7,12), Fraction(1,4), Fraction(-1,3)])
        self.assertEqual(im[2],[Fraction(1,12), Fraction(-1,4), Fraction(1,6)])
    


    def test_matr_multiply(self):
        m1=[[0.1, 0.4]]
        m2=[[2]]

        result = solution5.matrix_multiply(m2,m1)
        self.assertEqual(result[0],[0.2, 0.8])
    
    def test_calc_FR(self):
        R=[[Fraction(1,10), Fraction(4,10)]]
        Q= [[Fraction(1,2)]]

        result = solution5.calc_FR(R,Q)
        self.assertEqual(result[0],[Fraction(1,5), Fraction(4,5)])

    def test_case_1(self):
        m=[
        [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
        [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
        [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
        [0,0,0,0,0,0],  # s3 is terminal
        [0,0,0,0,0,0],  # s4 is terminal
        [0,0,0,0,0,0],  # s5 is terminal
        ]

        result = solution5.solution(m)
        self.assertEqual(result,[0,3,2,9,14])


    def test_case_2(self):
        m=[[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]
        result = solution5.solution(m)

        self.assertEqual(result,[7,6,8,21])

    def test_case_9(self):
        m=[[0, 86, 61, 189, 0, 18, 12, 33, 66, 39], [0, 0, 2, 0, 0, 1, 0, 0, 0, 0], [15, 187, 0, 0, 18, 23, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]        

        result = solution5.solution(m)
        self.assertEqual(result,[6, 44, 4, 11, 22, 13, 100])


    def test_case_10(self):
        m=[[0, 0, 0, 0, 3, 5, 0, 0, 0, 2], [0, 0, 4, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 4, 4, 0, 0, 0, 1, 1], [13, 0, 0, 0, 0, 0, 2, 0, 0, 0], [0, 1, 8, 7, 0, 0, 0, 1, 3, 0], [1, 7, 0, 0, 0, 0, 0, 2, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] 

        result = solution5.solution(m)
        self.assertEqual(result,[1, 1, 1, 2, 5])

    def test_case_8(self):
        m=[[1, 1, 1, 0, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        result = solution5.solution(m)
        self.assertEqual(result,[2, 1, 1, 1, 1, 6])

    def test_case_7(self):
        m=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        result = solution5.solution(m)
        self.assertEqual(result,[1, 1, 1, 1, 1, 5])

    def test_case_6(self):
        m=[[ 0,  7,  0, 17,  0,  1,  0,  5,  0,  2], [ 0,  0, 29,  0, 28,  0,  3,  0, 16,  0], [ 0,  3,  0,  0,  0,  1,  0,  0,  0,  0], [48,  0,  3,  0,  0,  0, 17,  0,  0,  0], [ 0,  6,  0,  0,  0,  1,  0,  0,  0,  0], [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0], [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0], [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0], [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0], [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0]]

        result = solution5.solution(m)
        self.assertEqual(result,[4, 5, 5, 4, 2, 20])
    
    def test_case_5(self):
        m=[[0, 0, 12, 0, 15, 0, 0, 0, 1, 8], [0, 0, 60, 0, 0, 7, 13, 0, 0, 0], [0, 15, 0, 8, 7, 0, 0, 1, 9, 0], [23, 0, 0, 0, 0, 1, 0, 0, 0, 0], [37, 35, 0, 0, 0, 0, 3, 21, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        result = solution5.solution(m)
        self.assertEqual(result,[1, 2, 3, 4, 5, 15])

    def test_case_4(self):
        m=[[0]]

        result = solution5.solution(m)
        self.assertEqual(result,[1, 1])



    def test_lcm_multi_14_3_7_6_shouldbe_42(self):
        result =solution5.lcm_multi([14,3,7,6])
        self.assertEqual(42,result)