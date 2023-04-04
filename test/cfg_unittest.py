import unittest
import os

if __name__ == "__main__":
    test_path = os.path.join(__file__, os.pardir)
    suite = unittest.TestLoader().discover(test_path, "test_*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
