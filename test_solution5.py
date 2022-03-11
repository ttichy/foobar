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

        result = solution5.get_R_Q_matrices(m,ab_states)
        Q=result[0]
        R=result[1]
        self.assertEqual(Q[0],[Fraction(1,2),0,0,0])
        self.assertEqual(Q[1],[0,Fraction(2,9),Fraction(1,3),0])
        
        self.assertEqual(R[0],[0,Fraction(1,2)])
        self.assertEqual(R[1],[Fraction(4,9),0])
