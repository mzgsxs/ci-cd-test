"""
Unit tests for the arithmetics library
"""

from mzgpaul_test_pkg import arithmetics


class TestArithmetics:
    def test_addition(self):
        assert arithmetics.add(2, 2) == 4

    def test_subtraction(self):
        assert arithmetics.subtract(4, 2) == 2

    def test_multiplication(self):
        assert arithmetics.multiply(10, 10) == 100
