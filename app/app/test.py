"""
This Module tests the calc function.
"""
from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Contains methods to test calc functions."""

    def test_add_numbers(self):
        """Test add function."""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Tests the subtract function."""
        res = calc.sub(5, 6)
        self.assertEqual(res, 1)
