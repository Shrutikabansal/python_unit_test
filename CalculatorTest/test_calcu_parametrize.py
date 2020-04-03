#import unittest
import calc
import pytest




@pytest.mark.parametrize('num1, num2, result',
 						[
 						(10, 7, 17),
 						("hii ", "user", "hii user"),
 						(10.5, 11.5, 22)
 						]	
						)
def test_add_positive_input(num1, num2, result):
   	assert calc.add(num1, num2)==result



#if __name__ == "__main__":
#	unittest.main()
