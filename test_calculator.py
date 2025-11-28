import unittest
from unittest.mock import patch
import math
import sys
import io

# Import the calculator module
sys.path.insert(0, 'c:\\Users\\andre\\OneDrive\\Documents\\Code Files\\Learning Code Files')

# Read and execute the calculator script to get its functions
calc_module_path = 'c:\\Users\\andre\\OneDrive\\Documents\\Code Files\\Learning Code Files\\Python Script.py'
with open(calc_module_path) as f:
    exec(f.read(), globals())


class TestPerformCalculation(unittest.TestCase):
    """Test suite for perform_calculation function"""

    def test_addition(self):
        """Test addition operation"""
        op_name, result = perform_calculation('1', 5, 3)
        self.assertEqual(op_name, 'Addition')
        self.assertEqual(result, 8)

    def test_addition_negative_numbers(self):
        """Test addition with negative numbers"""
        op_name, result = perform_calculation('1', -5, 3)
        self.assertEqual(op_name, 'Addition')
        self.assertEqual(result, -2)

    def test_addition_floats(self):
        """Test addition with floating point numbers"""
        op_name, result = perform_calculation('1', 5.5, 3.2)
        self.assertEqual(op_name, 'Addition')
        self.assertAlmostEqual(result, 8.7, places=5)

    def test_subtraction(self):
        """Test subtraction operation"""
        op_name, result = perform_calculation('2', 10, 3)
        self.assertEqual(op_name, 'Subtraction')
        self.assertEqual(result, 7)

    def test_subtraction_negative_result(self):
        """Test subtraction resulting in negative number"""
        op_name, result = perform_calculation('2', 3, 10)
        self.assertEqual(op_name, 'Subtraction')
        self.assertEqual(result, -7)

    def test_subtraction_floats(self):
        """Test subtraction with floating point numbers"""
        op_name, result = perform_calculation('2', 10.5, 3.2)
        self.assertEqual(op_name, 'Subtraction')
        self.assertAlmostEqual(result, 7.3, places=5)

    def test_multiplication(self):
        """Test multiplication operation"""
        op_name, result = perform_calculation('3', 5, 3)
        self.assertEqual(op_name, 'Multiplication')
        self.assertEqual(result, 15)

    def test_multiplication_by_zero(self):
        """Test multiplication by zero"""
        op_name, result = perform_calculation('3', 5, 0)
        self.assertEqual(op_name, 'Multiplication')
        self.assertEqual(result, 0)

    def test_multiplication_negative(self):
        """Test multiplication with negative numbers"""
        op_name, result = perform_calculation('3', -5, 3)
        self.assertEqual(op_name, 'Multiplication')
        self.assertEqual(result, -15)

    def test_multiplication_floats(self):
        """Test multiplication with floating point numbers"""
        op_name, result = perform_calculation('3', 5.5, 2.0)
        self.assertEqual(op_name, 'Multiplication')
        self.assertAlmostEqual(result, 11.0, places=5)

    def test_division(self):
        """Test division operation"""
        op_name, result = perform_calculation('4', 10, 2)
        self.assertEqual(op_name, 'Division')
        self.assertEqual(result, 5)

    def test_division_by_zero(self):
        """Test division by zero error handling"""
        op_name, result = perform_calculation('4', 10, 0)
        self.assertEqual(op_name, 'Division')
        self.assertIn('Error', result)
        self.assertIn('Division by zero', result)

    def test_division_floats(self):
        """Test division with floating point numbers"""
        op_name, result = perform_calculation('4', 10.5, 2.0)
        self.assertEqual(op_name, 'Division')
        self.assertAlmostEqual(result, 5.25, places=5)

    def test_division_negative(self):
        """Test division with negative numbers"""
        op_name, result = perform_calculation('4', -10, 2)
        self.assertEqual(op_name, 'Division')
        self.assertEqual(result, -5)

    def test_square_root_positive(self):
        """Test square root of positive number"""
        op_name, result = perform_calculation('5', 9, None)
        self.assertEqual(op_name, 'Square Root')
        self.assertEqual(result, 3)

    def test_square_root_zero(self):
        """Test square root of zero"""
        op_name, result = perform_calculation('5', 0, None)
        self.assertEqual(op_name, 'Square Root')
        self.assertEqual(result, 0)

    def test_square_root_one(self):
        """Test square root of one"""
        op_name, result = perform_calculation('5', 1, None)
        self.assertEqual(op_name, 'Square Root')
        self.assertEqual(result, 1)

    def test_square_root_float(self):
        """Test square root of floating point number"""
        op_name, result = perform_calculation('5', 16.0, None)
        self.assertEqual(op_name, 'Square Root')
        self.assertEqual(result, 4)

    def test_square_root_decimal(self):
        """Test square root resulting in decimal"""
        op_name, result = perform_calculation('5', 2, None)
        self.assertEqual(op_name, 'Square Root')
        self.assertAlmostEqual(result, math.sqrt(2), places=5)

    def test_square_root_negative(self):
        """Test square root of negative number error handling"""
        op_name, result = perform_calculation('5', -9, None)
        self.assertEqual(op_name, 'Square Root')
        self.assertIn('Error', result)
        self.assertIn('negative', result.lower())

    def test_large_numbers(self):
        """Test with large numbers"""
        op_name, result = perform_calculation('1', 1000000, 2000000)
        self.assertEqual(result, 3000000)

    def test_very_small_numbers(self):
        """Test with very small numbers"""
        op_name, result = perform_calculation('1', 0.001, 0.002)
        self.assertAlmostEqual(result, 0.003, places=5)


class TestDisplayResult(unittest.TestCase):
    """Test suite for display_result function"""

    def test_display_result_two_numbers(self):
        """Test display_result with two numbers"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        display_result('Addition', 5, 3, 8)
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn('Addition', output)
        self.assertIn('5', output)
        self.assertIn('3', output)
        self.assertIn('8', output)

    def test_display_result_one_number(self):
        """Test display_result with one number (square root)"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        display_result('Square Root', 9, None, 3)
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn('Square Root', output)
        self.assertIn('9', output)
        self.assertIn('3', output)
        self.assertNotIn('and', output)

    def test_display_result_with_error(self):
        """Test display_result with error message"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        display_result('Division', 10, 0, 'Error: Division by zero')
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn('Error', output)
        self.assertIn('Division by zero', output)


class TestGetOperation(unittest.TestCase):
    """Test suite for get_operation function"""

    @patch('builtins.input', return_value='1')
    def test_get_operation_valid_choice_1(self, mock_input):
        """Test getting operation choice 1"""
        result = get_operation()
        self.assertEqual(result, '1')

    @patch('builtins.input', return_value='5')
    def test_get_operation_valid_choice_5(self, mock_input):
        """Test getting operation choice 5"""
        result = get_operation()
        self.assertEqual(result, '5')

    @patch('builtins.input', side_effect=['invalid', '3'])
    def test_get_operation_invalid_then_valid(self, mock_input):
        """Test getting operation after invalid input"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        result = get_operation()
        sys.stdout = sys.__stdout__
        
        self.assertEqual(result, '3')
        self.assertIn('Invalid', captured_output.getvalue())

    @patch('builtins.input', side_effect=['6', '0', '-1', '2'])
    def test_get_operation_multiple_invalid_then_valid(self, mock_input):
        """Test getting operation after multiple invalid inputs"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        result = get_operation()
        sys.stdout = sys.__stdout__
        
        self.assertEqual(result, '2')


class TestGetNumbers(unittest.TestCase):
    """Test suite for get_numbers function"""

    @patch('builtins.input', side_effect=['5', '3'])
    def test_get_numbers_two_numbers(self, mock_input):
        """Test getting two numbers for binary operations"""
        num1, num2 = get_numbers('1')
        self.assertEqual(num1, 5.0)
        self.assertEqual(num2, 3.0)

    @patch('builtins.input', return_value='9')
    def test_get_numbers_square_root(self, mock_input):
        """Test getting one number for square root"""
        num1, num2 = get_numbers('5')
        self.assertEqual(num1, 9.0)
        self.assertIsNone(num2)

    @patch('builtins.input', side_effect=['-5.5', '3.2'])
    def test_get_numbers_negative_and_float(self, mock_input):
        """Test getting negative and floating point numbers"""
        num1, num2 = get_numbers('2')
        self.assertEqual(num1, -5.5)
        self.assertEqual(num2, 3.2)

    @patch('builtins.input', side_effect=['abc', '5', '10'])
    def test_get_numbers_invalid_then_valid(self, mock_input):
        """Test getting numbers after invalid input"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        num1, num2 = get_numbers('1')
        sys.stdout = sys.__stdout__
        
        self.assertEqual(num1, 5.0)
        self.assertEqual(num2, 10.0)
        self.assertIn('Invalid', captured_output.getvalue())

    @patch('builtins.input', side_effect=['abc', 'def', '5', '10'])
    def test_get_numbers_multiple_invalid_then_valid(self, mock_input):
        """Test getting numbers after multiple invalid inputs"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        num1, num2 = get_numbers('3')
        sys.stdout = sys.__stdout__
        
        self.assertEqual(num1, 5.0)
        self.assertEqual(num2, 10.0)

    @patch('builtins.input', side_effect=['0', '0'])
    def test_get_numbers_zeros(self, mock_input):
        """Test getting zeros as input"""
        num1, num2 = get_numbers('1')
        self.assertEqual(num1, 0.0)
        self.assertEqual(num2, 0.0)

    @patch('builtins.input', return_value='0')
    def test_get_numbers_square_root_zero(self, mock_input):
        """Test getting zero for square root"""
        num1, num2 = get_numbers('5')
        self.assertEqual(num1, 0.0)
        self.assertIsNone(num2)


class TestIntegration(unittest.TestCase):
    """Integration tests for complete calculation workflows"""

    def test_addition_workflow(self):
        """Test complete addition workflow"""
        with patch('builtins.input', side_effect=['5', '3']):
            num1, num2 = get_numbers('1')
        op_name, result = perform_calculation('1', num1, num2)
        self.assertEqual(result, 8)

    def test_square_root_workflow(self):
        """Test complete square root workflow"""
        with patch('builtins.input', return_value='16'):
            num1, num2 = get_numbers('5')
        op_name, result = perform_calculation('5', num1, num2)
        self.assertEqual(result, 4)

    def test_division_zero_error_workflow(self):
        """Test complete division by zero error workflow"""
        with patch('builtins.input', side_effect=['10', '0']):
            num1, num2 = get_numbers('4')
        op_name, result = perform_calculation('4', num1, num2)
        self.assertIn('Error', result)

    def test_negative_square_root_error_workflow(self):
        """Test complete negative square root error workflow"""
        with patch('builtins.input', return_value='-9'):
            num1, num2 = get_numbers('5')
        op_name, result = perform_calculation('5', num1, num2)
        self.assertIn('Error', result)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and boundary conditions"""

    def test_very_large_square_root(self):
        """Test square root of very large number"""
        op_name, result = perform_calculation('5', 1000000, None)
        self.assertAlmostEqual(result, 1000, places=1)

    def test_very_small_square_root(self):
        """Test square root of very small positive number"""
        op_name, result = perform_calculation('5', 0.0001, None)
        self.assertAlmostEqual(result, 0.01, places=5)

    def test_precision_loss_check(self):
        """Test for potential floating point precision loss"""
        # Adding then subtracting should (approximately) return to original
        sum_result = 1 + 0.1 + 0.2
        diff_result = sum_result - 0.1 - 0.2
        self.assertAlmostEqual(diff_result, 1.0, places=10)

    def test_very_large_numbers_multiplication(self):
        """Test multiplication of very large numbers"""
        op_name, result = perform_calculation('3', 1e10, 1e10)
        self.assertEqual(result, 1e20)

    def test_very_large_numbers_division(self):
        """Test division of very large numbers"""
        op_name, result = perform_calculation('4', 1e10, 2)
        self.assertEqual(result, 5e9)


if __name__ == '__main__':
    unittest.main()
