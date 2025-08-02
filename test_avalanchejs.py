# test_avalanchejs.py
"""
Tests for AvalancheJS module.
"""

import unittest
from avalanchejs import AvalancheJS

class TestAvalancheJS(unittest.TestCase):
    """Test cases for AvalancheJS class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AvalancheJS()
        self.assertIsInstance(instance, AvalancheJS)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AvalancheJS()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
