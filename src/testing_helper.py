###############################################################################
# STUDENTS:  IGNORE THIS MODULE (file).
# We use it in our testing code to make error messages appear in color.
###############################################################################

###############################################################################
# The code in this module is a simplified version of code written by:
#     dablak  (https://stackoverflow.com/users/1329248/dablak)
# That code appears at:
#    http://xsnippet.org/359377/
# and is referenced in dablak's question at:
#  https://stackoverflow.com/questions/20333674/pycharm-logging-output-colours.

# As with all user content to StackOverflow, it is licensed (by dablak) under:
#     CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
# a Creative Commons Attribution Share Alike license, as is this code.
###############################################################################

import sys
import time

PRECISION = 3  # Round floats to 3 decimal places when comparing vs expected

# Set  USE_COLORING  to False to use the "old" way of printing:
USE_COLORING = True

COLOR_CODES = {"black": 20,
               "red": 31,
               "green": 32,
               "yellow": 33,
               "blue": 34,
               "magenta": 35,
               "cyan": 36,
               "white": 37
               }


def print_expected_result_of_test(arguments, expected, test_results,
                                  format_string, suffix=""):
    test_number = test_results[0] + test_results[1] + 1
    print()
    print("Test {}:".format(test_number))

    print("  This test case calls:")
    print(format_string.format(*arguments))
    print("  Expected:", expected, suffix)


def print_actual_result_of_test(expected, actual, test_results, precision=None):
    print("  Actual:  ", actual)

    if USE_COLORING:
        print_it = print_colored
    else:
        print_it = print_uncolored

    try:
        if precision is not None:
            expected = round(expected, precision)
            actual = round(actual, precision)
        elif type(actual) is float:
            expected = round(expected, PRECISION)
            actual = round(actual, PRECISION)
        if expected == actual:
            print_it("  PASSED the above test -- good!", color="blue")
            test_results[0] = test_results[0] + 1
            return
        else:
            print_it("  *** FAILED the above test. ***", color="red")
    except Exception:
        print_it("  *** FAILED the above test. ***", color="red")
    test_results[1] = test_results[1] + 1


def print_summary_of_test_results(test_results):
    passed_tests = test_results[0]
    failed_tests = test_results[1]
    number_of_tests = failed_tests + passed_tests
    message_for_passed = "\n*** PASSED all {} tests! Good! ***"
    message_for_failed = "\n*** FAILED {} tests! ***"
    if passed_tests == number_of_tests:
        print_colored(message_for_passed.format(number_of_tests),
                      color="blue")
    else:
        print_colored(message_for_failed.format(failed_tests), color="red")


# noinspection PyUnusedLocal
def print_colored(*args, color="black", flush=True):
    text = ""
    for arg in args:
        text = text + " " + str(arg)
    text = text.replace(" ", "", 1) + "\n"
    sys.stdout.write("\033[%sm%s\033[0m" % (COLOR_CODES[color], text))


def print_uncolored(*args, color=None, flush=True):
    if color == "red":
        print(end="", flush=flush)
        time.sleep(1)
        print(*args, file=sys.stderr, flush=flush)  # Stderr MIGHT be red
    else:
        print(*args, flush=flush)
