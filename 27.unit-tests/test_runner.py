import unittest

from testing.test_models.test_user import test_password_validator_suite, user_test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(test_password_validator_suite())
    runner.run(user_test_suite())
