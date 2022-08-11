import unittest

class LoginTest(unittest.TestCase):
    def test_loginbyEmail(self):
        print("this test is login by Email")
        self.assertTrue(True)

    def test_loginbyFacebook(self):
        print("this test is login by facebook")
        self.assertTrue(True)

    def test_loginbyTwitter(self):
        print('this test is login by Facebook')
        self.assertTrue(True)

if __name__=="__main__":
     unittest.main()
