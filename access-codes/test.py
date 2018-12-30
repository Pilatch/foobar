# Inputs:
#     (string list) x = ["foo", "bar", "oof", "bar"]
# Output:
#     (int) 2

# Inputs:
#     (string list) x = ["x", "y", "xy", "yy", "", "yx"]
# Output:
#     (int) 5

import unittest
import solution


class AccessCodesTests(unittest.TestCase):

    def test_reverse(self):
        self.assertEqual("oof", solution._reverse("foo"))
        self.assertEqual("", solution._reverse(""))
        self.assertEqual("oooo", solution._reverse("oooo"))

    def test_get_palindrome_with_lower_half_first(self):
        self.assertEqual(
            "foooof", solution._get_palindrome_with_lower_half_first("foo"))
        self.assertEqual(
            "foooof", solution._get_palindrome_with_lower_half_first("oof"))
        self.assertEqual(
            "oooo", solution._get_palindrome_with_lower_half_first("oo"))
        self.assertEqual("", solution._get_palindrome_with_lower_half_first(""))
        self.assertEqual(
            "yy", solution._get_palindrome_with_lower_half_first("y"))

    def test_whole_enchilada(self):
        self.assertEqual( 5, solution.answer(["x", "y", "xy", "yy", "", "yx"]) )
        self.assertEqual( 2, solution.answer(["foo", "bar", "oof", "bar"]) )


if __name__ == '__main__':
    unittest.main()
