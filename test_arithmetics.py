"""
Unit tests for the arithmetics library
"""

import arithmetics


class TestArithmetics:

    def test_addition(self):
        assert 4 == arithmetics.add(2, 2)

    def test_subtraction(self):
        assert 2 == arithmetics.subtract(4, 2)
