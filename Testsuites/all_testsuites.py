import unittest

from package1.Tc_CarModelTest import CarModelTest
from package1.Tc_LocationTest import LocationTest

from package2.Tc_FoodTest import FoodTest
from package2.Tc_FruitTest import FruitTest

# get all TestCases
tc1=unittest.TestLoader().loadTestsFromTestCase(CarModelTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(LocationTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(FoodTest)
tc4=unittest.TestLoader().loadTestsFromTestCase(FruitTest)

# crerating testsuites

sanityTestsuite=unittest.TestSuite([tc1,tc2])

functionalTestsuite=unittest.TestSuite([tc3,tc4])

masterTestSuite=unittest.TestSuite([tc1,tc2,tc3,tc4])

unittest.TextTestRunner(verbosity=1).run(masterTestSuite)


