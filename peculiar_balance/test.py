# Inputs:
#     (int) x = 2
# Output:
#     (string list) ["L", "R"]

# Inputs:
#     (int) x = 8
# Output:
#     (string list) ["L", "-", "R"]

import unittest
import solution
Scale = solution.Scale
PowersOfThreeSequence = solution.PowersOfThreeSequence


class PeculiarBalanceTests(unittest.TestCase):

    def test_scale(self):
        self.assertTrue(Scale(0).is_balanced())
        scale_started_with_one_on_left = Scale(1)
        self.assertFalse(scale_started_with_one_on_left.is_balanced())
        scale_started_with_one_on_left.add_mass_to_right(1)
        self.assertTrue(scale_started_with_one_on_left.is_balanced())
        scale_started_with_four_on_left = Scale(4)
        self.assertEqual(4, scale_started_with_four_on_left.left_side_mass)
        self.assertEqual(0, scale_started_with_four_on_left.right_side_mass)
        self.assertFalse(scale_started_with_four_on_left.is_balanced())
        scale_started_with_four_on_left.add_mass_to_right(1)
        self.assertFalse(scale_started_with_four_on_left.is_balanced())
        scale_started_with_four_on_left.add_mass_to_right(3)
        self.assertTrue(scale_started_with_four_on_left.is_balanced())

    def test_powers_of_three_sequence(self):
        sequence = PowersOfThreeSequence()
        self.assertEqual(1, sequence.next())
        self.assertEqual(3, sequence.next())
        self.assertEqual(9, sequence.next())
        self.assertEqual(27, sequence.next())
        self.assertEqual(81, sequence.next())
        self.assertEqual(243, sequence.next())
        sequence = PowersOfThreeSequence(3)
        self.assertEqual(81, sequence.next())
        sequence = PowersOfThreeSequence(0)
        self.assertEqual(3, sequence.next())

    def test_take_commands(self):
        self.assertTrue(Scale(0).take_commands(()).is_balanced())
        self.assertTrue(Scale(1).take_commands(("R")).is_balanced())
        self.assertTrue(Scale(2).take_commands(("L", "R")).is_balanced())
        self.assertTrue(Scale(3).take_commands(("-", "R")).is_balanced())
        self.assertTrue(Scale(4).take_commands(("R", "R")).is_balanced())
        self.assertTrue(Scale(5).take_commands(("L", "L", "R")).is_balanced())
        self.assertTrue(Scale(6).take_commands(("-", "L", "R")).is_balanced())
        self.assertTrue(Scale(7).take_commands(("R", "L", "R")).is_balanced())
        self.assertTrue(Scale(8).take_commands(("L", "-", "R")).is_balanced())
        self.assertTrue(Scale(9).take_commands(("-", "-", "R")).is_balanced())
        self.assertTrue(Scale(10).take_commands(("R", "-", "R")).is_balanced())
        self.assertTrue(Scale(11).take_commands(("L", "R", "R")).is_balanced())
        self.assertTrue(Scale(12).take_commands(("-", "R", "R")).is_balanced())
        self.assertTrue(Scale(13).take_commands(("R", "R", "R")).is_balanced())
        self.assertTrue(
            Scale(14).take_commands(("L", "L", "L", "R")).is_balanced())
        self.assertTrue(
            Scale(15).take_commands(("-", "L", "L", "R")).is_balanced())
        self.assertTrue(
            Scale(16).take_commands(("R", "L", "L", "R")).is_balanced())
        self.assertTrue(
            Scale(17).take_commands(("L", "-", "L", "R")).is_balanced())
        self.assertTrue(
            Scale(18).take_commands(("-", "-", "L", "R")).is_balanced())
        self.assertTrue(
            Scale(19).take_commands(("R", "-", "L", "R")).is_balanced())
        self.assertTrue(
            Scale(20).take_commands(("L", "R", "L", "R")).is_balanced())
        self.assertTrue(
            Scale(21).take_commands(("-", "R", "L", "R")).is_balanced())
        self.assertTrue(
            Scale(22).take_commands(("R", "R", "L", "R")).is_balanced())
        self.assertTrue(
            Scale(23).take_commands(("L", "L", "-", "R")).is_balanced())
        self.assertTrue(
            Scale(24).take_commands(("-", "L", "-", "R")).is_balanced())
        self.assertTrue(
            Scale(25).take_commands(("R", "L", "-", "R")).is_balanced())
        self.assertTrue(
            Scale(26).take_commands(("L", "-", "-", "R")).is_balanced())
        self.assertTrue(
            Scale(27).take_commands(("-", "-", "-", "R")).is_balanced())
        self.assertTrue(
            Scale(28).take_commands(("R", "-", "-", "R")).is_balanced())
        self.assertTrue(
            Scale(29).take_commands(("L", "R", "-", "R")).is_balanced())
        self.assertTrue(
            Scale(30).take_commands(("-", "R", "-", "R")).is_balanced())
        self.assertTrue(
            Scale(31).take_commands(("R", "R", "-", "R")).is_balanced())
        self.assertTrue(
            Scale(32).take_commands(("L", "L", "R", "R")).is_balanced())
        self.assertTrue(
            Scale(33).take_commands(("-", "L", "R", "R")).is_balanced())
        self.assertTrue(
            Scale(34).take_commands(("R", "L", "R", "R")).is_balanced())
        self.assertTrue(
            Scale(35).take_commands(("L", "-", "R", "R")).is_balanced())
        self.assertTrue(
            Scale(36).take_commands(("-", "-", "R", "R")).is_balanced())
        self.assertTrue(
            Scale(37).take_commands(("R", "-", "R", "R")).is_balanced())
        self.assertTrue(
            Scale(38).take_commands(("L", "R", "R", "R")).is_balanced())
        self.assertTrue(
            Scale(39).take_commands(("-", "R", "R", "R")).is_balanced())
        self.assertTrue(
            Scale(40).take_commands(("R", "R", "R", "R")).is_balanced())
        self.assertTrue(
            Scale(41).take_commands(("L", "L", "L", "L", "R")).is_balanced())

    def test_largest_power_of_three_needed_to_balance(self):
        self.assertIsNone(Scale(0).largest_power_of_three_needed_to_balance())
        self.assertEqual(
            0, Scale(1).largest_power_of_three_needed_to_balance())
        self.assertEqual(
            1, Scale(2).largest_power_of_three_needed_to_balance())
        self.assertEqual(
            1, Scale(3).largest_power_of_three_needed_to_balance())
        self.assertEqual(
            1, Scale(4).largest_power_of_three_needed_to_balance())
        self.assertEqual(
            2, Scale(5).largest_power_of_three_needed_to_balance())
        self.assertEqual(
            2, Scale(6).largest_power_of_three_needed_to_balance())
        self.assertEqual(
            2, Scale(7).largest_power_of_three_needed_to_balance())
        self.assertEqual(
            2, Scale(8).largest_power_of_three_needed_to_balance())
        self.assertEqual(
            2, Scale(9).largest_power_of_three_needed_to_balance())
        self.assertEqual(
            2, Scale(10).largest_power_of_three_needed_to_balance())
        self.assertEqual(
            2, Scale(11).largest_power_of_three_needed_to_balance())
        self.assertEqual(
            2, Scale(12).largest_power_of_three_needed_to_balance())
        self.assertEqual(
            2, Scale(13).largest_power_of_three_needed_to_balance())
        self.assertEqual(
            3, Scale(14).largest_power_of_three_needed_to_balance())

    def test_largest_power_of_three_needed_to_balance_classmethod(self):
        self.assertEqual(
            2, Scale.largest_power_of_three_needed_to_balance_mass(13))
        self.assertEqual(
            3, Scale.largest_power_of_three_needed_to_balance_mass(14))

    def test_first_R_for_power_of_three_starts_at_mass(self):
        self.assertEqual(1, Scale.first_R_for_power_of_three_starts_at_mass(0))
        self.assertEqual(2, Scale.first_R_for_power_of_three_starts_at_mass(1))
        self.assertEqual(5, Scale.first_R_for_power_of_three_starts_at_mass(2))
        self.assertEqual(
            14, Scale.first_R_for_power_of_three_starts_at_mass(3))
        self.assertEqual(
            41, Scale.first_R_for_power_of_three_starts_at_mass(4))

    def test_make_command_list(self):
        self.assertEqual(["R", "L", "L", "R"], Scale(16).create_command_list())
        self.assertEqual(["L", "-", "R", "R"], Scale(35).create_command_list())

    def test_answer(self):
        self.assertEqual(["L", "R"], solution.answer(2))
        self.assertEqual(["L", "-", "R"], solution.answer(8))
        self.assert_commands_balance(
            (1000000000, 0, 1, 2, 3, 4, 5, 7, 11, 13, 14, 15, 20, 26, 27, 28, 78, 90, 99, 101, 240, 242, 243, 832, 777, 12345678))

    def assert_commands_balance(self, x_values_to_test):
        for x in x_values_to_test:
            scale = Scale(x)
            command_list = scale.create_command_list()
            self.assertTrue(scale.take_commands(command_list).is_balanced())

if __name__ == '__main__':
    unittest.main()
