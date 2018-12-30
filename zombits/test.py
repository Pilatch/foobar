# Inputs:
#     (double list) y = [1.0]
#     (double list) x = [1.0]
# Output:
#     (int) 0

# Inputs:
#     (double list) y = [2.2999999999999998, 15.0, 102.40000000000001, 3486.8000000000002]
#     (double list) x = [23.0, 150.0, 1024.0, 34868.0]
# Output:
#     (int) 90

import unittest
import solution

class ZombitsTests(unittest.TestCase):
  def test_one_oh(self):
    self.assertEqual( 0, solution.answer([1.0], [1.0]) )

  def test_more_complex(self):
    self.assertEqual( 90, solution.answer([2.2999999999999998, 15.0, 102.40000000000001, 3486.8000000000002], [23.0, 150.0, 1024.0, 34868.0]))

  def test_empty(self):
    self.assertIsNone( solution.answer([2], []) )
    self.assertIsNone( solution.answer([], [2]) )
    self.assertIsNone( solution.answer([], []) )

  def test_unequal_sizes(self):
    self.assertIsNone( solution.answer([2, 3], [1, 4, 9]) )

if __name__ == '__main__':
  unittest.main()