from main import returnBackwardsString, getMode
import unittest
import os

class TestMain(unittest.TestCase):
    def testReturnBackwardString(self):
        randomString = "This is my test string"
        randomStringReversed = "gnirts tset ym si sihT"
        self.assertEqual(randomStringReversed, returnBackwardsString(randomString))

    def testGetEnv(self):
        self.assertEqual(os.environ.get("MODE"), getMode())

if __name__ == "__main__":
    unittest.main()