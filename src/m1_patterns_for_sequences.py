"""
This module demonstrates and gives you practice at various patterns
for ITERATING through SEQUENCES, including these patterns:
  -- COUNT/SUM/EXAMINE-ITEMS
  -- FIND-ITEM
  -- FIND-BEST-ITEM
  -- TWO-PLACES-AT-EACH-ITERATION
  -- TWO-SEQUENCES-AT-EACH-ITERATION
  -- BUILD-A-SEQUENCE (in other modules of this session)

Of course, these are not the only patterns, and some problems require
combining these patterns, but this is a good base upon which to build.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import testing_helper
import time
import sys
import random


def main():
    """ Calls the   TEST   functions in this module. """
    print("-----------------------------------------------")
    print("Un-comment each of the following TEST functions")
    print("as you implement the functions that they test.")
    print("-----------------------------------------------")
    # run_test_count_sum_examine_items()
    # run_test_find_item()
    # run_test_find_best_item()
    # run_test_two_places_at_each_iteration()
    # run_test_two_sequences_at_each_iteration()


###############################################################################
# NOTE: In order to focus your attention on the CODE that you write using the
#   PATTERNS, the TESTING functions all appear at the BOTTOM of this module.
###############################################################################

# -----------------------------------------------------------------------------
# TODO: 2. Read the following, ASKING QUESTIONS AS NEEDED.
#  _
#  The   COUNT-SUM-EXAMINE-ITEMS   pattern loops through all or part of
#  the sequence, doing something with each item that it examines.
#  _
#  PATTERN:
#        for k in range(BLAH):
#            ... seq[k] ...
#  where BLAH is (in all of these patterns) some expression appropriate
#  as the range, e.g.
#        len(seq)
#  if the problem requires examining all the items in the sequence.
#  _
#  EXAMPLE:
#     Given a sequence of numbers,
#     return the number of items whose sine is positive.
#  _
#     count = 0
#     for k in range(len(numbers)):
#         if math.sin(numbers[k]) > 0:
#             count = count + 1
#     return count
#  _
#  After you are SURE that you understand the above, mark this _TODO_ as DONE.
# ----------------------------------------------------------------------------
def count_sum_examine_items(integers):
    """
    What comes in:  A sequence of positive integers
    What goes out:
      -- Returns the sum of integers in the sequence that are odd.
    Side effects:   None.
    Examples:
      -- If  integers  is  [20, 4, 7, 13, 3, 40, 25],
           this function returns  7 + 13 + 3 + 25, which is 48.
      -- If  integers  is   [],   this function returns 0.
      -- If  integers  is   [37], this function returns 37.
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #          The testing code is already written for you (below).
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# TODO: 4. Read the following, ASKING QUESTIONS AS NEEDED.
#  _
#  The   FIND-ITEM   pattern loops through the sequence but STOPPING when
#  it "finds" the first item of interest, returning whatever the problem says
#  to return in that case, or CONTINUING through the ENTIRE sequence, returning
#  whatever the problem says to return in the "not found" case.
#  _
#  PATTERN:
#        for k in range(BLAH):
#            if ... seq[k] ...:
#                return FOUND
#        return NOT-FOUND
#  _
#  where FOUND is whatever the problem says to return when an item of interest
#  is found, and NOT-FOUND is whatever the problem says to return when there
#  are NO items of interest found.
#  _
#  *** NOTE the placement/INDENTATION of the   RETURN   statements! ***
#  _
#  EXAMPLE:
#     Given a sequence of numbers,
#     return the first (i.e., lowest-index) item whose sine is positive,
#     or the string "OOPS" if no items in the sequence have positive sine.
#  _
#     for k in range(len(numbers)):
#         if math.sin(numbers[k]) > 0:
#             return numbers[k]
#     return "OOPS"
#  _
#  After you are SURE that you understand the above, mark this _TODO_ as DONE.
# ----------------------------------------------------------------------------
def find_item(numbers, threshold):
    """
    What comes in:  A sequence of numbers, and another number.
    What goes out:
      -- Returns the INDEX of the first (i.e., lowest-index) number
         of the sequence that is smaller than the given threshold,
         or -99 if no number in the sequence is smaller than the given
         threshold.
    Side effects:   None.
    Examples:
      -- find_item( [19, 32, 11, 6, 13, 6, 3, 14, 2],  10 )  returns  3
           because   6   is the first number in the sequence that is less
           than the threshold 10, and 6 is at index 3.
      -- find_item( [19, 32, 11, 6, 13, 6, 3, 14, 2],  2 )  returns  -99
           because no items in the sequence are less than the threshold 2
    """
    # -------------------------------------------------------------------------
    # TODO: 5. Implement and test this function.
    #          The testing code is already written for you (below).
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# TODO: 6. Read the following, ASKING QUESTIONS AS NEEDED.
#  _
#  The    FIND-BEST-ITEM   pattern finds the "best" item in a sequence.
#  In its simplest form, the    FIND-BEST-ITEM   pattern:
#    1. Starts with the item at index 0 as its "best-so-far" item.
#    2. Continues by looping through the rest of the sequence.
#         Every time that it encounters an item that is "better" than its
#         "best-so-far" item, it reassigns its "best-so-far" variable
#         to refer to the newly-found "better" item.
#    3. Returns the "best-so-far" value after completing the loop.
#  _
#  However, some problems require the returning the INDEX of the "best" item,
#  so the following pattern stores the INDEX of the "best-so-far" item rather
#  than the item itself:
#  _
#  PATTERN:
#        index_of_best_so_far = 0
#        for k in range(1, len(seq)):
#            if ... seq[k]   is "better" than   seq[index_of_best_so_far]
#                index_of_best_so_far = k
#        return BEST
#  _
#  where BEST is either the INDEX of the "best" item in the sequence
#  or the "best" item itself, depending on what the problem demands.
#  _
#  EXAMPLE:
#     Given a sequence of numbers,
#     return the index of the item whose sine is smallest.
#     (Break ties in favor of the smallest-index item.)
#  _
#     index_of_best_so_far = 0
#     for k in range(1, len(numbers)):
#         if math.sin(numbers[k]) < math.sin(numbers[index_of_best_so_far]):
#             index_of_best_so_far = k
#     return index_of_best_so_far
#  _
#  After you are SURE that you understand the above, mark this _TODO_ as DONE.
# ----------------------------------------------------------------------------
def find_best_item(integers):
    """
    What comes in:  A non-empty sequence of positive integers
    What goes out:
      -- Returns the item in the sequence whose sum-of-digits is biggest.
           (Break ties in favor of the smallest-index item.)
    Side effects:   None.
    Examples:
      -- find_best_item( [74, 102, 901, 98, 11, 22, 773] )  returns  98
           because the:
             -- sum-of-digits of 75   is 11 (74, at index 0, is best so far,
                                             with 11 as its sum-of-digits)
             -- sum-of-digits of 102  is 3  (NOT bigger than 11)
             -- sum-of-digits of 901  is 10 (NOT bigger than 11)
             -- sum-of-digits of 98   is 17 (98, at index 3, is best so far,,
                                             with 17 as its sum-of-digits)
             -- sum-of-digits of 11   is 2  (NOT bigger than 17)
             -- sum-of-digits of 22   is 4  (NOT bigger than 17)
             -- sum-of-digits of 773  is 17  (TIED, but NOT bigger than 17)
    """
    # -------------------------------------------------------------------------
    # TODO: 7. Implement and test this function.
    #          The testing code is already written for you (below).
    #  *** The usual   sum_of_digits   function is defined further below.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# TODO: 8. Read the following, ASKING QUESTIONS AS NEEDED.
#  _
#  The   TWO-PLACES-AT-EACH-ITERATION    pattern loops through the sequence,
#  but at each iteration it examines TWO items, at two DIFFERENT indices.
#  _
#  PATTERN:
#        for k in range( BLAH ):
#            ... sequence[ INDEX_1 ] ... sequence[ INDEX_2 ] ...
#  _
#  where BLAH is some range appropriate to the problem,
#       INDEX_1 is some function of k that gives ONE
#             of the "two places at each iteration" to examine, and
#       INDEX_2 is another function of k that gives the OTHER
#             of the "two places at each iteration" to examine.
#  Typically, INDEX_1 or INDEX_2 (but not both) is simply k.
#  _
#  EXAMPLE:
#     Given a sequence of numbers,
#     return the number of places in the sequence where the number at one
#     place is greater than the number at the next place.
#  _
#     count = 0
#     for k in range(len(numbers) - 1):
#         if numbers[k] > numbers[k + 1]:
#             count = count + 1
#     return count
#  _
#  After you are SURE that you understand the above, mark this _TODO_ as DONE.
# ----------------------------------------------------------------------------
def two_places_at_each_iteration(numbers):
    """
    What comes in:  A non-empty sequence of numbers.
    What goes out:
      -- Returns True if the sequence is in ascending order,
         else returns False.
    Side effects:   None.
    Examples:
      -- two_places_at_each_iteration( [19, 23, 23, 45, 50] )  returns  True
      -- two_places_at_each_iteration( [19, 23, 20, 45, 42] )  returns  False
    """
    # -------------------------------------------------------------------------
    # TODO: 9. Implement and test this function.
    #          The testing code is already written for you (below).
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# TODO: 10. Read the following, ASKING QUESTIONS AS NEEDED.
#  _
#  The   TWO-SEQUENCES-AT-EACH-ITERATION    pattern
#  loops through TWO (or more) sequences "in parallel".
#  _
#  PATTERN:
#        for k in range(len(sequence_1)):
#            ... sequence_1[k] ... sequence_2[k] ...
#  _
#  The above assumes that the sequences are of equal length
#  (or that you just want to do the length of sequence_1).
#  _
#  EXAMPLE:
#     Given two sequences of numbers,
#     return the number of places where the item in the first sequence
#     is greater than the same-index item in the second sequence.
#  _
#     count = 0
#     for k in range(len(numbers_1)):
#         if numbers_1[k] > numbers_2[k]:
#             count = count + 1
#     return count
#  _
#  After you are SURE that you understand the above, mark this _TODO_ as DONE.
# ----------------------------------------------------------------------------
def two_sequences_at_each_iteration(numbers_1, numbers_2):
    """
    What comes in:  Two sequences of numbers, each of the same length.
    What goes out:
      -- Returns the sum of items, where each item to be summed
         is the smaller of the same-index items in the two sequences.
    Side effects:   None.
    Examples:
      -- two_sequences_at_each_iteration( [5, 2, 7, 11, 8, 20],
                                          [9, 1, 3, 20, 9, 40] )
                 returns  5 + 1 + 3 + 11 + 8 + 20, which is 48
      -- two_sequences_at_each_iteration( [10, 5, 8, 4],
                                          [20, 3, 8, 100] )
                 returns  10 + 3 + 8 + 4, which is 25
      -- two_sequences_at_each_iteration( [20, 3, 8, 100],
                                          [10, 5, 8, 4])
                 returns  10 + 3 + 8 + 4, which is 25
    """
    # -------------------------------------------------------------------------
    # TODO: 11. Implement and test this function.
    #          The testing code is already written for you (below).
    # -------------------------------------------------------------------------


def run_test_count_sum_examine_items():
    """ Tests the   count_sum_examine_items   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   count_sum_examine_items   function:")
    print("--------------------------------------------------")

    format_string = '    count_sum_examine_items( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    sequence = [20, 4, 7, 13, 3, 40, 25]
    expected = 48
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = count_sum_examine_items(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    sequence = []
    expected = 0
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = count_sum_examine_items(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    sequence = [37]
    expected = 37
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = count_sum_examine_items(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    sequence = [38]
    expected = 0
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = count_sum_examine_items(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    sequence = [21, 4, 13, 3, 40, 25, 27, 31]
    expected = 120
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = count_sum_examine_items(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    sequence = [22, 4, 13, 3, 40, 25, 27, 31]
    expected = 99
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = count_sum_examine_items(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    sequence = [22, 4, 13, 3, 40, 25, 27, 32]
    expected = 68
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = count_sum_examine_items(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    sequence = range(1, 101, 2)
    expected = 2500
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = count_sum_examine_items(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    sequence = range(2, 101, 4)
    expected = 0
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = count_sum_examine_items(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    sequence = range(1, 10000, 3)
    expected = 8333333
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = count_sum_examine_items(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)


def run_test_find_item():
    """ Tests the   find_item   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   find_item   function:")
    print("--------------------------------------------------")

    format_string = '    find_item( {}, {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    sequence = [19, 32, 11, 6, 13, 6, 3, 14, 2]
    threshold = 10
    expected = 3
    print_expected_result_of_test([sequence, threshold], expected, test_results,
                                  format_string)
    actual = find_item(sequence, threshold)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    sequence = [19, 32, 11, 6, 13, 6, 3, 14, 2]
    threshold = 2
    expected = -99
    print_expected_result_of_test([sequence, threshold], expected, test_results,
                                  format_string)
    actual = find_item(sequence, threshold)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    sequence = [19, 12, 31]
    threshold = 20
    expected = 0
    print_expected_result_of_test([sequence, threshold], expected, test_results,
                                  format_string)
    actual = find_item(sequence, threshold)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    sequence = [29, 12, 11]
    threshold = 20
    expected = 1
    print_expected_result_of_test([sequence, threshold], expected, test_results,
                                  format_string)
    actual = find_item(sequence, threshold)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    sequence = [29, 42, 11]
    threshold = 20
    expected = 2
    print_expected_result_of_test([sequence, threshold], expected, test_results,
                                  format_string)
    actual = find_item(sequence, threshold)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    sequence = [29, 42, 21]
    threshold = 20
    expected = -99
    print_expected_result_of_test([sequence, threshold], expected, test_results,
                                  format_string)
    actual = find_item(sequence, threshold)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    sequence = list(range(100, 200)) + list(range(300, 50, -3))
    threshold = 100
    expected = 167
    print_expected_result_of_test([sequence, threshold], expected, test_results,
                                  format_string)
    actual = find_item(sequence, threshold)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    sequence = list(range(100, 200)) + list(range(300, 50, -3))
    threshold = 101
    expected = 0
    print_expected_result_of_test([sequence, threshold], expected, test_results,
                                  format_string)
    actual = find_item(sequence, threshold)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    sequence = list(range(100, 200)) + list(range(300, 50, -3))
    threshold = 99
    expected = 168
    print_expected_result_of_test([sequence, threshold], expected, test_results,
                                  format_string)
    actual = find_item(sequence, threshold)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    sequence = list(range(100, 200)) + list(range(300, 50, -3))
    threshold = 52
    expected = 183
    print_expected_result_of_test([sequence, threshold], expected, test_results,
                                  format_string)
    actual = find_item(sequence, threshold)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    sequence = list(range(100, 200)) + list(range(300, 50, -3))
    threshold = 51
    expected = -99
    print_expected_result_of_test([sequence, threshold], expected, test_results,
                                  format_string)
    actual = find_item(sequence, threshold)
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)


def run_test_find_best_item():
    """ Tests the   find_best_item   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   find_best_item   function:")
    print("--------------------------------------------------")

    format_string = '    find_best_item( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    sequence = [74, 102, 901, 98, 11, 22, 773]
    expected = 98
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = find_best_item(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    sequence = [88, 103, 99, 77, 89, 100]
    expected = 99
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = find_best_item(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    sequence = [99, 103, 88, 77, 89, 100]
    expected = 99
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = find_best_item(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    sequence = [88, 99, 103, 77, 89, 100]
    expected = 99
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = find_best_item(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    sequence = [88, 103, 77, 99, 89, 100]
    expected = 99
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = find_best_item(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    sequence = [88, 103, 89, 77, 99, 100]
    expected = 99
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = find_best_item(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    sequence = [88, 103, 89, 77, 100, 99]
    expected = 99
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = find_best_item(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    sequence = [100000]
    expected = 100000
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = find_best_item(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    sequence = [100000, 11]
    expected = 11
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = find_best_item(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    sequence = [88, 11, 22, 33, 44, 55, 66]
    expected = 88
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = find_best_item(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    sequence = [88, 11, 22, 33, 44, 55, 66]
    expected = 88
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = find_best_item(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Tests 11 to 30 (pseudo-random tests):
    random.seed(42)  # Set the seed so that tests are repeatable
    for k in range(5, 25):
        length = k  # Make sequences whose lengths vary from 5 to 25
        sequence = []
        for j in range(length):
            # Fill the sequence with random numbers where each random umber
            # is either between 10 and 50 or between 90 and 94
            # All such numbers have sum of digits less than 14
            if random.randrange(2) == 0:
                new_item = random.randrange(10, 50)
            else:
                new_item = random.randrange(90, 94)
            sequence.append(new_item)
        # Insert a number whose sum of digits is at least 14 (hence best)
        # at a random place in the sequence:
        possibles = [68, 69, 77, 78, 79, 86, 87, 88, 89]
        best = possibles[random.randrange(len(possibles))]
        sequence.insert(random.randrange(len(sequence) + 1), best)

        sequence.append(68)  # 2nd best at end

        expected = best
        print_expected_result_of_test([sequence], expected, test_results,
                                      format_string)
        actual = find_best_item(sequence)
        print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)


def run_test_two_places_at_each_iteration():
    """ Tests the   two_places_at_each_iteration   function. """
    print()
    print("------------------------------------------------------")
    print("Testing the   two_places_at_each_iteration   function:")
    print("------------------------------------------------------")

    format_string = '    two_places_at_each_iteration( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    sequence = [19, 23, 23, 45, 50]
    expected = True
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = two_places_at_each_iteration(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    sequence = [19, 23, 20, 45, 42]
    expected = False
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = two_places_at_each_iteration(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    sequence = [-100, -50, -34, -2, 0, 0, 0, 0, 1, 3, 3]
    expected = True
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = two_places_at_each_iteration(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    sequence = [-100, -50, -34, -2, 0, 0, 0, -1, 1, 3, 3]
    expected = False
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = two_places_at_each_iteration(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    sequence = [-100, -150, -34, -2, 0, 0, 0, -1, 1, 3, 3]
    expected = False
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = two_places_at_each_iteration(sequence)
    print_actual_result_of_test(expected, actual, test_results)
    print_summary_of_test_results(test_results)

    # Test 6:
    sequence = [-100, -50, -34, -2, 0, 0, 0, -1, 1, 3, 3, -100000]
    expected = False
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = two_places_at_each_iteration(sequence)
    print_actual_result_of_test(expected, actual, test_results)
    print_summary_of_test_results(test_results)

    # Test 7:
    sequence = [1, 1, 1, 2, 2, 3, 100000]
    expected = True
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = two_places_at_each_iteration(sequence)
    print_actual_result_of_test(expected, actual, test_results)
    print_summary_of_test_results(test_results)

    # Test 8:
    sequence = [-100001, -100000]
    expected = True
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = two_places_at_each_iteration(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)


def run_test_two_sequences_at_each_iteration():
    """ Tests the   two_sequences_at_each_iteration   function. """
    print()
    print("------------------------------------------------------")
    print("Testing the   two_sequences_at_each_iteration   function:")
    print("------------------------------------------------------")

    format_string = '    two_sequences_at_each_iteration( {}, {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    sequence_1 = [5, 2, 7, 11, 8, 20]
    sequence_2 = [9, 1, 3, 20, 9, 40]
    expected = 5 + 1 + 3 + 11 + 8 + 20  # which is 48
    print_expected_result_of_test([sequence_1, sequence_2], expected,
                                  test_results, format_string)
    actual = two_sequences_at_each_iteration(sequence_1, sequence_2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    sequence_1 = [10, 5, 8, 4]
    sequence_2 = [20, 3, 8, 100]
    expected = 10 + 3 + 8 + 4  # which is 25
    print_expected_result_of_test([sequence_1, sequence_2], expected,
                                  test_results, format_string)
    actual = two_sequences_at_each_iteration(sequence_1, sequence_2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    sequence_1 = [20, 3, 8, 100]
    sequence_2 = [10, 5, 8, 4]
    expected = 10 + 3 + 8 + 4  # which is 25
    print_expected_result_of_test([sequence_1, sequence_2], expected,
                                  test_results, format_string)
    actual = two_sequences_at_each_iteration(sequence_1, sequence_2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    sequence_1 = [5, 200, 7, 11, 8, 20, 10, 14, 101]
    sequence_2 = [1, -10, 5, 20, 9, 40, 10, 20, 100]
    expected = 1 + -10 + 5 + 11 + 8 + 20 + 10 + 14 + 100  # which is 159
    print_expected_result_of_test([sequence_1, sequence_2], expected,
                                  test_results, format_string)
    actual = two_sequences_at_each_iteration(sequence_1, sequence_2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    sequence_1 = [5]
    sequence_2 = [1]
    expected = 1
    print_expected_result_of_test([sequence_1, sequence_2], expected,
                                  test_results, format_string)
    actual = two_sequences_at_each_iteration(sequence_1, sequence_2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    sequence_1 = [1]
    sequence_2 = [5]
    expected = 1
    print_expected_result_of_test([sequence_1, sequence_2], expected,
                                  test_results, format_string)
    actual = two_sequences_at_each_iteration(sequence_1, sequence_2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    sequence_1 = [10, 20, 30, 40, 50]
    sequence_2 = [-1, -1, -1, -1, -1]
    expected = -5
    print_expected_result_of_test([sequence_1, sequence_2], expected,
                                  test_results, format_string)
    actual = two_sequences_at_each_iteration(sequence_1, sequence_2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    sequence_1 = [10, 20, 30, 20, 10, 5, 4, 3, 2]
    sequence_2 = [-9, 19, 25, 15, 20, 9, 9, 9, 0]
    expected = -9 + 19 + 25 + 15 + 10 + 5 + 4 + 3 + 0  # which is 72
    print_expected_result_of_test([sequence_1, sequence_2], expected,
                                  test_results, format_string)
    actual = two_sequences_at_each_iteration(sequence_1, sequence_2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    sequence_1 = [-9, 19, 25, 15, 20, 9, 9, 9, 0]
    sequence_2 = [10, 20, 30, 20, 10, 5, 4, 3, 2]
    expected = -9 + 19 + 25 + 15 + 10 + 5 + 4 + 3 + 0  # which is 72
    print_expected_result_of_test([sequence_1, sequence_2], expected,
                                  test_results, format_string)
    actual = two_sequences_at_each_iteration(sequence_1, sequence_2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    sequence_1 = [5, 200, 7, 11, 8, 20, 10, 14, -1010]
    sequence_2 = [1, -10, 5, 20, 9, 40, 10, 20, -1000]
    expected = 1 + -10 + 5 + 11 + 8 + 20 + 10 + 14 + -1010  # which is -951
    print_expected_result_of_test([sequence_1, sequence_2], expected,
                                  test_results, format_string)
    actual = two_sequences_at_each_iteration(sequence_1, sequence_2)
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)


def sum_of_digits(number):
    """
    What comes in:  An integer.
    What goes out:  Returns the sum of the digits in the given integer.
    Side effects:   None.
    Example:
      If the integer is 83135,
      this function returns (8 + 3 + 1 + 3 + 5), which is 20.
    """
    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  sum_of_digits function - it has no _TODO_.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # -------------------------------------------------------------------------
    if number < 0:
        number = -number

    digit_sum = 0
    while True:
        if number == 0:
            break
        digit_sum = digit_sum + (number % 10)
        number = number // 10

    return digit_sum


###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################

def print_expected_result_of_test(arguments, expected,
                                  test_results, format_string, suffix=''):
    testing_helper.print_expected_result_of_test(arguments, expected,
                                                 test_results, format_string,
                                                 suffix)


def print_actual_result_of_test(expected, actual, test_results,
                                precision=None):
    testing_helper.print_actual_result_of_test(expected, actual,
                                               test_results, precision)


def print_summary_of_test_results(test_results):
    testing_helper.print_summary_of_test_results(test_results)


# To allow color-coding the output to the console:
USE_COLORING = True  # Change to False to revert to OLD style coloring

testing_helper.USE_COLORING = USE_COLORING
if USE_COLORING:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_colored
else:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_uncolored

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
try:
    main()
except Exception:
    print('ERROR - While running this test,', color='red')
    print('your code raised the following exception:', color='red')
    print()
    sys.stdout.flush()
    time.sleep(1)
    raise
