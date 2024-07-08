# """
# This module contains unit tests for the application.
# """
# # Import only the necessary components
# from django.test import TestCase
# # Add your test cases here
# class SampleTestCase(TestCase):
#     def test_example(self):
#         # self.assertEqual(1 + 1, 2)
"""
This module contains unit tests for the application.
"""
from django.test import TestCase
class SampleTestCase(TestCase):
    """Test case for basic example tests."""
    def test_example(self):
        """Test that 1 + 1 equals 2."""
        self.assertEqual(1 + 1, 2)
