''' Template for unit testing with Python's unittest module.

    https://realpython.com/python-testing/ 
    https://notesfromthelifeboat.com/post/testing-arcpy-2/ 
'''


# Imports 
import unittest
from unittest.mock import Mock 
''' For the purpose of unit testing, we assume that 
    any third party APIs like arcpy work as expected. 
    We only need to test our own custom logic. Mocks enable this. 

    Mocks substitute the behaviour of any object in a flexible way. 

    https://realpython.com/python-mock-library/ 
'''
arcpy = Mock()              # Instead of 'import arcpy' for global use
from toolLogic import *     # Import the logic that you want to test 


''' MyToolTestCase contains your individual tests.
    
    Any functions whose names begin with 'test' will be run automatically
    as part of the test case. 
''' 
class MyToolTestCase(unittest.TestCase):

    def testThisIsAPassingTest(self):
        '''Unit tests use assertions to test behaviour of your code'''
        self.assertEqual(1, 1) # True, this test will pass

    def testThisIsAFailingTest(self):
        '''A simple example of a failing test'''
        self.assertNotEqual(1, 1) # Fake news, this test will fail

    def testSpecialThing(self):
        '''You can check that a function returns the expected value''' 
        expected = 'Did a special thing'
        self.assertEqual(
            specialThing(), # Whatever the function returns
            expected        # Your expected result - is it equal? 
        )
    
    def testAnotherSpecialThingWithString(self): 
        ''' More usefully, check an input returns the expected result.
            anotherSpecialThing returns the type of the input argument.  
        '''
        argument = 'a string'
        expected = str # Represents Python's built-in string type 
        self.assertEqual(
            anotherSpecialThing(argument),
            expected
        )
    
    def testDoComplicatedArcpyAnalysis(self):
        ''' Remember that we don't usually want to invoke arcpy in our tests.
            However, we might want to confirm that Buffer_analysis gets 
            called with the correct arguments. 

            Because we have assigned a Mock object to a variable named 
            arcpy (on line 19), and will pass it to doComplicatedArcpyAnalysis
            in place of the real arcpy module, we can get the Mock object to 
            check that our function gives Buffer_analysis the expected 
            parameters. 
        '''
        # Declare input arguments - these don't need to exist on disk
        in_fc = 'C:\\data.gdb\\my_input_fc'
        out_fc = 'C:\\data.gdb\\my_output_fc'
        distance = '500 Miles'
        # Invoke function with these arguments and our arcpy Mock
        doComplicatedArcpyAnalysis(in_fc, out_fc, distance, arcpy)
        # Use Mock's assert_called_with method to check the Buffer arguments
        arcpy.Buffer_analysis.assert_called_with(
            in_fc,
            out_fc, 
            distance
        )


if __name__ == '__main__':
    ''' This runs the test case which will report the results of your tests.

        If you run this now, you should see the following result in your 
        console: 
        
        ======================================================================
        FAIL: testThisIsAFailingTest (__main__.MyToolTestCase)
        A simple example of a failing test
        ----------------------------------------------------------------------
        Traceback (most recent call last):
        File "c:/Users/cronind/repos/PerfectScriptTool/toolTest.py", line 35, in testThisIsAFailingTest
            self.assertNotEqual(1, 1) # Fake news, this test will fail
        AssertionError: 1 == 1

        ----------------------------------------------------------------------
        Ran 5 tests in 0.013s

        FAILED (failures=1)
    '''
    unittest.main() # Kick things off 
