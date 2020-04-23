''' This is the test runner. It can run tests from several test cases,
    all in one convenient place. 

    Just run this file to check that everything is OK. 

    Remember that there is one example of a failing test in toolTest.py, 
    so don't be alarmed when this fails. 

    https://realpython.com/python-testing/#choosing-a-test-runner 
'''

import unittest

# Import your test modules
import toolTest

# Initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# Add tests to the test suite
suite.addTests(loader.loadTestsFromModule(toolTest))

# Initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)

''' Expected result: 

    testAnotherSpecialThingWithString (toolTest.MyToolTestCase)
    More usefully, check an input returns the expected result. ... ok
    testDoComplicatedArcpyAnalysis (toolTest.MyToolTestCase)
    Remember that we don't usually want to invoke arcpy in our tests. ... ok
    testSpecialThing (toolTest.MyToolTestCase)
    You can check that a function returns the expected value ... ok
    testThisIsAFailingTest (toolTest.MyToolTestCase)
    A simple example of a failing test ... FAIL
    testThisIsAPassingTest (toolTest.MyToolTestCase)
    Unit tests use assertions to test behaviour of your code ... ok

    ======================================================================
    FAIL: testThisIsAFailingTest (toolTest.MyToolTestCase)
    A simple example of a failing test
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    File "c:\Users\cronind\repos\PerfectScriptTool\toolTest.py", line 36, in testThisIsAFailingTest
        self.assertNotEqual(1, 1) # Fake news, this test will fail
    AssertionError: 1 == 1

    ----------------------------------------------------------------------
    Ran 5 tests in 0.005s

    FAILED (failures=1)
'''