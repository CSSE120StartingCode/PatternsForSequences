"""
This module lets you practice various patterns
for ITERATING through SEQUENCES, including:
  -- Beginning to end
  -- Other ranges (e.g., backwards and every-3rd-item)
  -- The COUNT/SUM/etc pattern
  -- The FIND pattern (via LINEAR SEARCH)

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_radii()
    run_test_count_last_n_odds()
    run_test_index_of_first_negative()
    run_test_contains_an_a()


# ----------------------------------------------------------------------
# Many problems simply iterate (loop) through ALL of the sequence,
# as in the  sum_radii  problem below.
# ----------------------------------------------------------------------
def run_test_sum_radii():
    """ Tests the   sum_radii   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_radii   function:')
    print('--------------------------------------------------')

    # Test 1 is ALREADY DONE (here).
    print()
    circle1 = rg.Circle(rg.Point(100, 100), 25)
    circle2 = rg.Circle(rg.Point(100, 100), 50)
    circle3 = rg.Circle(rg.Point(100, 100), 10)

    expected = 85
    seq = (circle1, circle2, circle3)
    actual = sum_radii(seq)
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 2 is ALREADY DONE (here).
    print()
    circle1 = rg.Circle(rg.Point(200, 20), 80)
    circle2 = rg.Circle(rg.Point(300, 100), 60)
    circle3 = rg.Circle(rg.Point(100, 150), 0)
    circle4 = rg.Circle(rg.Point(0, 0), 30)

    expected = 170
    seq = (circle1, circle2, circle3, circle4)
    actual = sum_radii(seq)
    print('Expected:', expected)
    print('Actual:  ', actual)


def sum_radii(circles):
    """
    What comes in:
      -- a sequence of rg.Circle objects
    What goes out:
      Returns the sum of the radii of the given sequence of rg.Circles.
    Side effects: None.
    Example:  If
          circle1 = rg.Circle(rg.Point(999, 100), 25)
          circle2 = rg.Circle(rg.Point(888, 200), 50)
          circle3 = rg.Circle(rg.Point(777, 300), 10)
      then   sum_radii([circle1, circle2, circle3])
      returns 25 + 50 + 10, which is 85.
    Type hints:
      :type circles:  list | tuple of rg.Circle
      :rtype: int | float
    """
    # ------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #     The testing code is already written for you (above).
    #
    # Note: No fair using "slices" on ANY of these problems,
    #       if you happen to know what they are.
    #
    #       Likewise, no fair using any builtin methods on sequences
    #       or strings, if you happen to know any.
    #
    #       Instead, use explicit loops, as you have for other problems.
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Some problems iterate (loop) through PART of the sequence,
# perhaps BACKWARDS, as in the   count_last_n_odds   problem below.
# ----------------------------------------------------------------------
def run_test_count_last_n_odds():
    """ Tests the   count_last_n_odds   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   count_last_n_odds   function:')
    print('--------------------------------------------------')

    # Six tests - ALREADY DONE (here).
    seq = [1, 5, 88, 44, 33, 77, 10, 12, 9]
    answer1 = count_last_n_odds(seq, 0)
    answer2 = count_last_n_odds(seq, 1)
    answer3 = count_last_n_odds(seq, 6)
    answer4 = count_last_n_odds(seq, 7)
    answer5 = count_last_n_odds(seq, 8)
    answer6 = count_last_n_odds(seq, 9)

    print()
    print('Test set #1 of count_last_n_odds:',
          answer1, answer2, answer3, answer4, answer5, answer6)
    print('The above should be:              0 1 3 3 4 5')

    # Six more tests - ALREADY DONE (here).
    seq = [17, 88, -5, -10, 0]
    answer1 = count_last_n_odds(seq, 0)
    answer2 = count_last_n_odds(seq, 1)
    answer3 = count_last_n_odds(seq, 2)
    answer4 = count_last_n_odds(seq, 3)
    answer5 = count_last_n_odds(seq, 4)
    answer6 = count_last_n_odds(seq, 5)

    print()
    print('Test set #2 of count_last_n_odds:',
          answer1, answer2, answer3, answer4, answer5, answer6)
    print('The above should be:              0 0 0 1 1 2')


def count_last_n_odds(integers, n):
    """
    What comes in:
      -- a sequence of integers
      -- a non-negative integer  n  that is less than or equal to
           the length of the given sequence
    What goes out:  Returns the number of odd integers
      in the last n items of the given sequence.
    Side effects: None.
    Examples:
      If the sequence is (13, 66, 15, 3), then:
       count_last_n_odds(sequence, 0) is 0  [no odds]
       count_last_n_odds(sequence, 1) is 1  [1 odd, namely 3]
       count_last_n_odds(sequence, 2) is 2  [2 odds, namely 3 and 15]
       count_last_n_odds(sequence, 3) is 2  [2 odds, namely 3 and 15]
       count_last_n_odds(sequence, 4) is 3  [3 odds: 3, 15 and 13]
    Type hints:
      :type integers: list | tuple of int
      :type n: int
      :rtype: int
    """
    # ------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #     The testing code is already written for you (above).
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Some problems iterate (loop) through PART of the sequence,
# stopping when the loop FINDS something of interest
# (or continuing to the end if it does NOT find the thing of interest),
# as in the following problems:
# ----------------------------------------------------------------------
def run_test_index_of_first_negative():
    """ Tests the   index_of_first_negative   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   index_of_first_negative   function:')
    print('--------------------------------------------------')

    # Test 1:
    print()
    expected = 3
    actual = index_of_first_negative([90, 0, 20, -5, 30, -10, 15])
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 2:
    print()
    expected = 0
    actual = index_of_first_negative([-5, 30, -10, 15])
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 3:
    print()
    expected = 4
    actual = index_of_first_negative([5, 30, 10, 15, -1])
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 4:
    print()
    expected = -1
    actual = index_of_first_negative([5, 30, 10, 15, 1, 6])
    print('Expected:', expected)
    print('Actual:  ', actual)
    if actual == '-1':
        print('  Your answer is WRONG.')
        print('  You returned the STRING \'-1\'')
        print('  when you should have returned just -1')


def index_of_first_negative(numbers):
    """
    What comes in:
      -- a sequence of numbers
    What goes out: Returns the INDEX of the first negative number
      in the given sequence of numbers, or -1 if the sequence
      contains no negative numbers.
      Note: "first" negative number means the negative number
      whose index is smallest -- see the examples.
    Side effects: None.
    Examples: If the argument is:
      -- [4, 30, -19, 8, -3, -50, 100], this function returns 2
            since the first negative number is -19, which is at index 2

      -- [-8, 44, 33], this function returns 0
            since the first negative number is -8, which is at index 0

      -- [1, 29, 22, 8], this function returns -1
            since the list contains no negative numbers
    Type hints:
      :type numbers: list | tuple of float | int
      :rtype: int
    """
    # ------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    #     The testing code is already written for you (above).
    # ------------------------------------------------------------------


def run_test_contains_an_a():
    """ Tests the   contains_an_a   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   contains_an_a   function:')
    print('--------------------------------------------------')

    # Tests:
    actual1 = contains_an_a('nope')
    actual2 = contains_an_a('yes a is here')
    actual3 = contains_an_a('many aaaaas aaa aaa')
    actual4 = contains_an_a('not until the very end is a')
    actual5 = contains_an_a('a @ the beginning')
    actual6 = contains_an_a('')
    actual7 = contains_an_a('BLAH BLAH BLAH')
    actual8 = contains_an_a('BLAH BLAH BLAH \t MORE BLAH')
    actual9 = contains_an_a('BLAH BLAH BLAH \t MORE BLaH')

    actuals = (actual1, actual2, actual3, actual4, actual5, actual6,
               actual7, actual8, actual9)
    expecteds = (False, True, True, True, True, False,
                 False, False, True)

    for k in range(len(actuals)):
        print()
        print('Expected:', expecteds[k])
        print('Actual:  ', actuals[k])
        if type(actuals[k]) is str and str(expecteds[k]) == actuals[k]:
            print('Your code FAILED this test for   contains_an_a.')
            print('  You appear to have returned the STRING:')
            print('      "' + actuals[k] + '"')
            print('  instead of the built-in constant:')
            print('       ' + str(expecteds[k]))


def contains_an_a(s):
    """
    What comes in:
      -- a string
    What goes out: Returns  True  if the given string contains
      the character 'a'.  Returns  False  if the given string
      does not contain the character 'a'.
    Side effects: None.
    Examples:
      -- contains_an_a('blah blah blah')  returns True
      -- contains_an_a('BLAH BLAH BLAH')  returns False
      -- contains_an_a('abc')             returns True
      -- contains_an_a('')                returns False
    Type hints:
      :type s: str
      :rtype: bool
    """
    # ------------------------------------------------------------------
    # TODO: 5. Implement and test this function.
    #     The testing code is already written for you (above).
    #
    ####################################################################
    # IMPORTANT:
    #   -- True  and  False  are built-in constants.
    #      Do NOT return the STRINGs 'True' and 'False'.
    ####################################################################
    #
    # Implementation requirement:
    #   Use an explicit loop, as you have done in the other problems.
    #   No fair using the   count   or   find   string methods.
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
