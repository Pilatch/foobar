# Hmmm... passing "self" all over the place isn't DRY.
# I guess the tradeoff is that static members don't have to specify self like in Ruby...
# Unless you want to create a @classmethod, then you have to specify any(!?) class as the first argument.
# By contrast, I can make a Ruby module without using self, then extend that module in a class.
# So Ruby's still coming out ahead in that regard.
# And no private thingies? I can privately encapsulate even in JavaScript.
# Boo.
# I guess the real savings is the lack of curly braces or "end".
# So my favorite feature so far is the indentation.
#
# Anyhow, this question seemed tough at first,
# but really boiled down to pattern recognition and abstraction.
# In the end I fought more with the language than with the math. 
# I'm used to integer division resulting in floats without explicit conversion
# probably because of all the JavaScript I've been writing lately.
# 
# Certainly I'm not as smart as Beta Bunny because my solution doesn't seem elegant,
# though it appears to be fast enough to calculate the command list for one billion in just a few milliseconds.
# If I remember right, you need eighteen powers of three to add up to one billion.
# For seventeen of those you have to perform a few division operations.
# You get the biggest "R" by doing division and rounding eighteen times.
# I'm not about to calculate the big O,
# but it looks like a tiny fraction of the input for large inputs, so log(n).
# I feel like there's still redundancy in there somewhere,
# but I should get back to finding jobs.
# 
# Interesting problem!
import math


def answer(x):
    return Scale(x).create_command_list()


class Scale():

    def __init__(self, left_side_mass):
        self.left_side_mass = left_side_mass
        self.right_side_mass = 0

    def add_mass_to_left(self, mass):
        self.left_side_mass += mass

    def add_mass_to_right(self, mass):
        self.right_side_mass += mass

    def is_balanced(self):
        return self.left_side_mass == self.right_side_mass

    @classmethod
    def first_R_for_power_of_three_starts_at_mass(cls, power_of_three):
        return int(math.ceil(3 ** power_of_three / 2.0))

    @classmethod
    def largest_power_of_three_needed_to_balance_mass(cls, mass):
        if mass < 1:
            return None
        sequence = PowersOfThreeSequence()
        while math.ceil(sequence.next() / 2.0) <= mass:
            pass
        return sequence.current_power - 1

    def largest_power_of_three_needed_to_balance(self):
        return self.__class__.largest_power_of_three_needed_to_balance_mass(self.left_side_mass)

    def take_commands(self, commands):
        sequence = PowersOfThreeSequence()
        for command in commands:
            mass = sequence.next()
            if command == "L":
                self.add_mass_to_left(mass)
            elif command == "R":
                self.add_mass_to_right(mass)
            elif command != "-":
                raise Exception("Unsupported scale command '" + command + "'")
        return self

    def create_command_list(self):
        command_list = []
        if self.left_side_mass == 0:
            return command_list
        # given a mass, find the largest power of three necessary
        largest_power_needed = self.largest_power_of_three_needed_to_balance()
        # we unshift in an R for that power
        command_list.insert(0, "R")
        # create a sequence at the previous power, then back your way through
        # it
        sequence = PowersOfThreeSequence(largest_power_needed - 1)
        while sequence.current_power != -1:
            # Subtract the starting R's mass for this power from the left side mass.
            # This gives us the non-blank depth in that power's column.
            # Each column has the pattern RL-, with each character appearing sequence-mass number of times.
            # So we divide by sequence-mass to determine where this scale's left-side mass falls within that pattern.
            # Finally we do modular division by 3 to get our answer.
            # Refer to the "mass command lists" comments at the bottom to understand the pattern.
            starting_mass_for_power = self.__class__.first_R_for_power_of_three_starts_at_mass(
                sequence.current_power)
            non_blank_depth_in_power_column = self.left_side_mass - \
                starting_mass_for_power + 1
            command_pattern_index = math.ceil(
                float(non_blank_depth_in_power_column) / sequence.mass()) % 3
            if command_pattern_index == 1:
                command_list.insert(0, "R")
            elif command_pattern_index == 2:
                command_list.insert(0, "L")
            elif command_pattern_index == 0:
                command_list.insert(0, "-")
            else:
                raise Exception(
                    "Unexpected command_pattern_index " + command_pattern_index)
            sequence.previous()
        return command_list


class PowersOfThreeSequence():

    def __init__(self, starting_power=-1):
        self.current_power = starting_power

    def next(self):
        self.current_power += 1
        return self.mass()

    def previous(self):
        self.current_power -= 1
        return self.mass()

    def mass(self):
        return 3 ** self.current_power

#mass command lists:
#  0         
#  1 R       
#  2 L R     
#  3 - R     
#  4 R R     
#  5 L L R   
#  6 - L R   
#  7 R L R   
#  8 L - R   
#  9 - - R   
# 10  R - R   
# 11  L R R   
# 12  - R R   
# 13  R R R   
# 14  L L L R 
# 15  - L L R 
# 16  R L L R 
# 17  L - L R 
# 18  - - L R 
# 19  R - L R 
# 20  L R L R 
# 21  - R L R 
# 22  R R L R 
# 23  L L - R 
# 24  - L - R 
# 25  R L - R 
# 26  L - - R 
# 27  - - - R 
# 28  R - - R 
# 29  L R - R 
# 30  - R - R 
# 31  R R - R 
# 32  L L R R 
# 33  - L R R 
# 34  R L R R 
# 35  L - R R 
# 36  - - R R 
# 37  R - R R 
# 38  L R R R 
# 39  - R R R 
# 40  R R R R 
# 41  L L L L R
