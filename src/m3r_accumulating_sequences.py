"""
This module demonstrates BUILDING-UP a new SEQUENCE,
one item at a time, using the ACCUMULATOR pattern.
  -- We will later see a more efficient way to build-up and/or modify
        sequences, namely by MUTATING their elements.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.


# -----------------------------------------------------------------------------
# TODO: 2. READ the program below and RUN it.
#   ___
#   When you have read it, asking questions as needed,
#   and you feel that you understand,
#   for each of LISTS, STRINGS and TUPLES:
#      -- HOW to BUILD UP them, using the ACCUMULATOR pattern.
#      -- when the   str   function is needed, and why,
#   then:
#      change the above _TODO_ to DONE.
# -----------------------------------------------------------------------------


def main():
    """
    Demonstrates building sequences by using the Accumulator pattern.
    """
    print()
    print("-----------------------------------------------------------")
    print("Build and then print a LIST:")
    print("-----------------------------------------------------------")
    build_list()

    print()
    print("-----------------------------------------------------------")
    print("Build and then print a TUPLE:")
    print("-----------------------------------------------------------")
    build_tuple()

    print()
    print("-----------------------------------------------------------")
    print("Build and then print a STRING:")
    print("-----------------------------------------------------------")
    build_string()


def build_list():
    """
    Demonstrates building a new LIST by using the Accumulator pattern.
    We will later see a more efficient way to build/modify lists,
    namely, by mutating the elements of the list.
    """
    # -------------------------------------------------------------------------
    # Here is the Accumulator pattern for building up LISTs:
    #
    #   1. BEFORE the loop, initialize the list variable
    #         (the "accumulator") to the empty list [].
    #
    #   2. LOOP, appending items one at a time (each time thru the loop)
    #
    #   3. INSIDE the loop:
    #
    #        a. Use   +  to concatenate:
    #             -- the existing list, and (followed by)
    #             -- the one-element list containing the new item
    #           thus constructing a new list with the new item appended.
    #
    #        b. Re-assign the list variable to the NEW list.
    #
    #   4. AFTER the loop, the variable is the entire "built up" list.
    # -------------------------------------------------------------------------
    """ This example builds (and then prints) the LIST
        [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] """
    sequence = []
    for k in range(10):
        sequence = sequence + [k ** 2]

    print(sequence)


def build_tuple():
    """
    Demonstrates building a TUPLE by using the Accumulator pattern.
      -- A tuple is just like a list except:
           1. It is IMMUTABLE, which means that its elements cannot be
                changed (more on that later), and
           2. Its notation uses ()s instead of []s.  Also,
                a one-element tuple requires a COMMA after the item.
    """
    # -------------------------------------------------------------------------
    # The Accumulator pattern for building up TUPLEs
    # is the same as for LISTs except:
    #   -- Initialize the list variable (the "accumulator")
    #         to the empty TUPLE () instead of the empty LIST [].
    #   -- Concatenate the one-element TUPLE:   (blah,)
    #         instead of the one-element LIST:  [blah]
    #         NOTE the COMMA required for a one-element tuple.
    # -------------------------------------------------------------------------
    """ This example builds (and then prints) the TUPLE
        (0, 1, 4, 9, 16, 25, 36, 49, 64, 81) """
    sequence = ()
    for k in range(10):
        sequence = sequence + (k ** 2,)

    print(sequence)


def build_string():
    """
    Demonstrates building a STRING by using the Accumulator pattern.
    We will later see a more efficient way to build/modify strings,
    namely, by using the  split/join   methods.
    """
    # -------------------------------------------------------------------------
    # The Accumulator pattern for building up STRINGs
    # is the same as for LISTs except:
    #   -- Initialize the list variable (the "accumulator")
    #         to the empty STRING "" instead of the empty LIST [].
    #   -- Concatenate the one (or more) element STRING:   "blah"
    #         instead of the one-element LIST:  [blah]
    #
    # The built-in   str   function returns a string version
    # of its argument.
    # -------------------------------------------------------------------------
    """ This example builds (and then prints) the STRING
        0 1 4 9 16 25 36 49 64 81 """
    sequence = ""
    for k in range(10):
        sequence = sequence + str(k ** 2) + " "

    print(sequence)


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
