import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class FruitTest(unittest.TestCase):
    def test_Mango(self):
        serv_obj = Service("C:\DRIVER\chromedriver_win32\chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.get("https://www.healthline.com/nutrition/mango")
        fruits=self.driver.title
        print(fruits)
        self.assertNotEqual("delicous",fruits)
        self.driver.get_screenshot_as_file("C:\DRIVERS\mango.png")
        print("the indian summer fruit")
        print("excuted succefully")
if __name__=="__main__":
    unittest.main()
