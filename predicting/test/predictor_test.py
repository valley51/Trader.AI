'''
Created on 08.11.2017

Module for testing of all predicting components

@author: jtymoszuk
'''
import unittest

from predicting.simple_predictor import SimplePredictor
from datetime import date


class PredictingTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
       
    def testSimplePredictor(self):
        sp = SimplePredictor()     
        
        inputData = list()
        
        today = date(2017, 11, 8)
        yesterday = date(2017, 11, 8)
        
        tuple1 = (yesterday, 2.0)
        tuple2 = (today, 3.0)
        
        inputData.append(tuple1)
        inputData.append(tuple2)

        result = sp.doPredict(inputData)
        
        self.assertEqual(result, 3.0)

    
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(PredictingTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
