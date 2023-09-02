import unittest
from cascading_palindrome import CascadingPalindrome

class TestCascadingPalindrome(unittest.TestCase):
    
    def test_single_word_palindrome(self):
        cp = CascadingPalindrome("1230321")
        self.assertEqual(cp.find_palindrome(), "1230321")

    def test_multiple_words_with_palindrome(self):
        cp = CascadingPalindrome("1230321 09234 0124210")
        self.assertEqual(cp.find_palindrome(), "1230321")

    def test_multiple_words_with_multiple_palindromes(self):
        cp = CascadingPalindrome("abcd5dcba 1230321 09234 0124210")
        self.assertEqual(cp.find_palindrome(), "abcd5dcba")

    def test_no_palindromes(self):
        cp = CascadingPalindrome("not a palindrome")
        self.assertEqual(cp.find_palindrome(), "")

    def test_empty_input(self):
        cp = CascadingPalindrome("")
        self.assertEqual(cp.find_palindrome(), "")

    def test_whitespace_input(self):
        cp = CascadingPalindrome("      ")
        self.assertEqual(cp.find_palindrome(), "")

    def test_special_characters(self):
        cp = CascadingPalindrome("@@a!@")
        self.assertEqual(cp.find_palindrome(), "a")

    def test_mixed_case(self):
        cp = CascadingPalindrome("AbcDcBa 1230321 09234 0124210")
        self.assertEqual(cp.find_palindrome(), "AbcDcBa")

    def test_non_alphanumeric(self):
        cp = CascadingPalindrome("123 321 !@# 999")
        self.assertEqual(cp.find_palindrome(), "!@#")

    def test_invalid_input_type(self):
        with self.assertRaises(ValueError):
            cp = CascadingPalindrome(123)  # Input must be a string

    def test_invalid_component_type(self):
        with self.assertRaises(ValueError):
            cp = CascadingPalindrome("valid 123 456")  # Components must be strings

if __name__ == "__main__":
    unittest.main()


