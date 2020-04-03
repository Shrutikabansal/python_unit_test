import unittest
import cmath

def add(x,y):
        if type(x) not in [int,float] or type(y) not in [int,float]:
                raise TypeError("Input is a string, change the input")
        return x+y

def sub(x,y):
        if type(x) not in [int,float] or type(y) not in [int,float]:
                raise TypeError("Input is a string, change the input")
        return x-y


def mult(x,y):
        if type(x) not in [int,float] or type(y) not in [int,float]:
                raise TypeError("Input is a string, change the input")
        return x*y

     
def div(x,y):
        if type(x) not in [int,float] or type(y) not in [int,float]:
                raise TypeError("Input is a string, change the input")

        elif(y==0):
                raise TypeError("y=0, change the input")

        return x/y







class TestCalcu_add(unittest.TestCase):
        def test_add_positive_input(self):
                self.assertEqual(add(1,5),6)
               # print("test_mult_positive_input passed")
        def test_add_negative_input(self):
                self.assertEqual(add(-1,-5),-6)
                #print("test_mult_positive_input passed")
     
        def test_add_float_input(self):
                self.assertEqual(add(-0.2,-0.12),-0.32)
                
        def test_add_both_input(self):
                self.assertEqual(add(-1,1.5),0.5)
     
        def test_add_invalid_string_input(self):
                self.assertRaises(TypeError,mult,1,"string")
     
        def test_add_invalid_list_input(self):
                self.assertRaises(TypeError,mult,[1,5],[1])
     
        def test_add_invalid_boolean_input(self):
                self.assertRaises(TypeError,mult,True,False)
     
        def test_add_invalid_complex_input(self):
                self.assertRaises(TypeError,mult,complex(4,2),complex(7,8))










class TestCalcu_sub(unittest.TestCase):
        def test_sub_positive_input(self):
                self.assertEqual(sub(1,5),-4)
               # print("test_mult_positive_input passed")
        def test_sub_negative_input(self):
                self.assertEqual(sub(-1,-5),4)
                #print("test_mult_positive_input passed")
     
        def test_sub_float_input(self):
                self.assertEqual(sub(-0.11,0.21),-0.32)
                
        def test_sub_both_input(self):
                self.assertEqual(sub(-1,1.5),-2.5)
     
        def test_sub_invalid_string_input(self):
                self.assertRaises(TypeError,sub,1,"string")
     
        def test_sub_invalid_list_input(self):
                self.assertRaises(TypeError,sub,[1,5],[1])
     
        def test_sub_invalid_boolean_input(self):
                self.assertRaises(TypeError,sub,True,False)
     
        def test_sub_invalid_complex_input(self):
                self.assertRaises(TypeError,sub,complex(4,2),complex(7,8))



     

class TestCalcu_mult(unittest.TestCase):
        def test_mult_positive_input(self):
                self.assertEqual(mult(1,5),5)
               # print("test_mult_positive_input passed")
        def test_mult_negative_input(self):
                self.assertEqual(mult(-1,-5),5)
                #print("test_mult_positive_input passed")
     
        def test_mult_float_input(self):
                self.assertEqual(mult(-0.2,-0.12),0.024)
                
        def test_mult_both_input(self):
                self.assertEqual(mult(-1,1.5),-1.5)
     
        def test_mult_invalid_string_input(self):
                self.assertRaises(TypeError,mult,1,"string")
     
        def test_mult_invalid_list_input(self):
                self.assertRaises(TypeError,mult,[1,5],[1])
     
        def test_mult_invalid_boolean_input(self):
                self.assertRaises(TypeError,mult,True,False)
     
        def test_mult_invalid_complex_input(self):
                self.assertRaises(TypeError,mult,complex(4,2),complex(7,8))






class TestCalcu_div(unittest.TestCase):
        def test_div_positive_input(self):
                self.assertEqual(div(1,5),0)
               # print("test_mult_positive_input passed")
        def test_div_negative_input(self):
                self.assertEqual(div(-1,-5),0)
                #print("test_mult_positive_input passed")
     
        def test_div_float_input(self):
                self.assertEqual(div(-0.2,-0.1),2)
                
        def test_div_both_input(self):
                self.assertEqual(div(-1.5,1),-1.5)

        def test_div_both_input_1(self):
                self.assertEqual(div(-1,0.2),-5)
     
        def test_div_invalid_string_input(self):
                self.assertRaises(TypeError,div,1,"string")
     
        def test_div_invalid_list_input(self):
                self.assertRaises(TypeError,div,[1,5],[1])
     
        def test_div_invalid_boolean_input(self):
                self.assertRaises(TypeError,div,True,False)
     
        def test_div_invalid_complex_input(self):
                self.assertRaises(TypeError,div,complex(4,2),complex(7,8))

        def test_div_invalid_y_input(self):
                self.assertRaises(TypeError,div,4,0)



if __name__ == "__main__":
	unittest.main()
