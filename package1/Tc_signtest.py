import unittest

class SignTest(unittest.TestCase):
    def test_signbyEmail(self):
        print("this test is sign by Email")
        self.assertTrue(True)

    def test_signbyFacebook(self):
        print("this test is sign by Facebook")
        self.assertTrue(True)

    def test_signbyTwitter(self):
        print("this test is sign by Twitter")
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()
