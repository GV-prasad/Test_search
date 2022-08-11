import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class FoodTest(unittest.TestCase):
    def test_ChickenBiryani(self):
        serv_obj=Service("C:\DRIVER\chromedriver_win32\chromedriver.exe")
        self.driver=webdriver.Chrome(service=serv_obj)
        self.driver.get("https://www.indianhealthyrecipes.com/chicken-biryani-recipe/")
        dish=self.driver.title
        print(dish)
        self.assertFalse(dish== "mocktail")
        self.driver.get_screenshot_as_file("C:\DRIVERS\CB.png")
        print("the indians most favourite dish")

    def test_Falooda(self):
        serv_obj=Service("C:\DRIVER\chromedriver_win32\chromedriver.exe")
        self.driver=webdriver.Chrome(service=serv_obj)
        self.driver.get('https://www.indianhealthyrecipes.com/falooda-recipe/')
        drink=self.driver.title
        print(drink)
        self.assertFalse(drink== "carlsburg")
        self.driver.get_screenshot_as_file("C:\DRIVERS\Falooda.png")
        print("the famous drink in india")

if __name__ =="__main__":
    unittest.main()
