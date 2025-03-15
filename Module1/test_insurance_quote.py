"""
* Name         : test_insurance_quote.py
* Author       : E Wilber
* Created      : 01/19/25
* Module       : 1
* Topic        : 4
* Description  : Tests for Insurance Quote Assignment
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""
import unittest
import unittest.mock as mock
import insurance_quote as quote

class MyTestCase(unittest.TestCase):

    def test_nameInput(self):
        with mock.patch('builtins.input', return_value="E"):
            assert quote.get_name() == "E"

    def test_ageInput(self):
        with mock.patch('builtins.input', return_value=24):
            assert quote.get_age() == 24

    def test_coverageInput(self):
        with mock.patch('builtins.input', return_value="F"):
            assert quote.get_coverage() == "f"

    def test_accidentsInput(self):
        with mock.patch('builtins.input', return_value="no"):
            assert quote.has_accidents() == False

    def test_discountInput(self):
        with mock.patch('builtins.input', return_value="No"):
            assert quote.wants_upfront_discount() == False

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)