import unittest
import calc
import cmath




class TestCalcu_add(unittest.TestCase):
        def test_add_string(self):
                self.assertEqual(calc.add("Hii ","User"),"Hii User")
               # print("test_mult_positive_input passed")




class TestCalcu_mult(unittest.TestCase):
        def test_mult_string(self):
                self.assertEqual(calc.mult("Hii ",2),"Hii Hii ")
               # print("test_mult_positive_input passed")





if __name__ == "__main__":
	unittest.main()
