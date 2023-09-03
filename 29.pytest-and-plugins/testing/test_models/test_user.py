import os
import sys
import unittest
from unittest import TestCase

from models.user import User, password_validator, hash_password


class UserTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User("username", "pwd")

    def test_del_password(self):
        user = self.user
        self.assertIsNotNone(user.password)
        del user.password
        self.assertIsNone(user.password)

    def test_set_passwords(self):
        passwords = [
            (
                "qwerty",
                "65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5",
            ),
            (
                "abc",
                "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
            ),
            (None, None),
            (
                "",
                "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            ),
        ]
        for pwd, expected in passwords:
            with self.subTest(pwd=pwd):
                self.user.password = pwd
                self.assertEqual(self.user.password, expected)


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
        print("check not win")
        self.assertIn("ix", os.name)

    @unittest.skipUnless(sys.platform == "darwin", "Run tests for macOS")
    def test_for_mac(self):
        self.assertEqual(os.name, "posix")


class TestPasswordValidator:
    def test_password_validator_ok(self):
        pwd = "qwerty"
        hashed_pwd = hash_password(pwd)
        assert password_validator(pwd, hashed_pwd) is True


def test_password_validator_ok_func():
    pwd = "qwerty"
    hashed_pwd = hash_password(pwd)
    assert password_validator(pwd, hashed_pwd) is True
