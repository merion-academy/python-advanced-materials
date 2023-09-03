import os
import sys
import unittest
from unittest import TestCase

from models.user import User, password_validator, hash_password


def setUpModule():
    print("set up (create connection to db)")


def tearDownModule():
    print("tear down (close connection)")


class UserTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    def setUp(self) -> None:
        self.user = User("username", "pwd")

    def tearDown(self) -> None:
        print("delete user", self.user.username)
        # self.user.delete()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_del_password(self):
        user = self.user
        self.assertIsNotNone(user.password)
        del user.password
        self.assertIsNone(user.password)


class PasswordValidatorTestCase(TestCase):
    def test_password_validator_ok(self):
        pwd = "qwerty"
        hashed_pwd = hash_password(pwd)
        self.assertTrue(password_validator(pwd, hashed_pwd))

    def test_password_validator_doesnt_match(self):
        pwd = "qwerty"
        self.assertFalse(password_validator(pwd, pwd))

    @unittest.skip("not ready yet")
    def test_fails(self):
        assert False

    @unittest.skipIf(sys.platform.startswith("win"), "Runs not on Windows")
    def test_all_but_windows(self):
        self.assertIn("ix", os.name)

    @unittest.skipUnless(sys.platform == "darwin", "Run tests for macOS")
    def test_for_mac(self):
        self.assertEqual(os.name, "posix")


def test_password_validator_func():
    pwd = "qwerty"
    hashed_pwd = hash_password(pwd)
    assert password_validator(pwd, hashed_pwd) is True


pwd_validator_test_case = unittest.FunctionTestCase(
    testFunc=test_password_validator_func,
    # setUp=...,
    # tearDown=...,
)


def test_password_validator_suite():
    suite = unittest.TestSuite()

    suite.addTest(pwd_validator_test_case)
    return suite


def user_test_suite():
    suite = unittest.TestSuite()
    suite.addTest(pwd_validator_test_case)

    suites = [suite]
    test_loader = unittest.TestLoader()

    suites.append(
        test_loader.loadTestsFromTestCase(UserTestCase),
    )

    suites.append(
        test_loader.loadTestsFromTestCase(PasswordValidatorTestCase),
    )

    return unittest.TestSuite(suites)
