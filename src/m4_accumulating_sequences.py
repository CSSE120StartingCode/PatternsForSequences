"""
This module lets you practice BUILDING-UP a new SEQUENCE,
one item at a time, using the ACCUMULATOR pattern.
  -- We will later see a more efficient way to build-up and/or modify
        sequences, namely by MUTATING their elements.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the various   TEST   functions in this module. """
    run_test_make_simple_list()
    run_test_make_simple_string()
    run_test_make_less_simple_string()

    # -------------------------------------------------------------------------
    # TODO: 8. Uncomment the tests below before working _TODO_ 9.
    #   They launch annoying rg.RoseWindows on each run that you don't want
    #   until you get to _TODO_ 9 and _TODO_ 10.
    # -------------------------------------------------------------------------
    # run_test_draw_shapes()
    # run_test_rectangles_from_circles()


def run_test_make_simple_list():
    """ Tests the   make_simple_list    function. """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement this TEST function.
    #   It TESTS the  make_simple_list  function defined below.
    #   Include at least **   2   ** tests.
    #   ___
    #   Use the same 4-step process as for previous TEST functions.
    # -------------------------------------------------------------------------
    print()
    print("--------------------------------------------------")
    print("Testing the   make_simple_list   function:")
    print("--------------------------------------------------")

    # Test 1:
    expected = [5, 6, 7, 8, 9, 10, 11, 12, 13]
    actual = make_simple_list(5, 13)
    print("Expected:", expected)
    print("Actual:  ", actual)

    # -------------------------------------------------------------------------
    # TODO: 2 (continued)
    #  Test 2:  (YOU write THIS test)
    # -------------------------------------------------------------------------


def make_simple_list(m, n):
    """
    What comes in:
      -- a positive integer m
      -- a positive integer n that is >= m
    What goes out:  Returns the list [m, m+1, m+2, ... n],
        where m and n are the given arguments.
    Side effects:   None.
    Examples:
      If m is 5 and n is 13, then this function returns:
        [5, 6, 7, 8, 9, 10, 11, 12, 13]

      If m and n are both 205, then this function returns:  [205]

    Type hints:
      :type m: int
      :type n: int
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    # -------------------------------------------------------------------------


def run_test_make_simple_string():
    """ Tests the   make_simple_string    function. """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement this TEST function.
    #   It TESTS the  make_simple_string  function defined below.
    #   Include at least **   2   ** tests.
    #   ___
    #   Use the same 4-step process as for previous TEST functions.
    # -------------------------------------------------------------------------
    print()
    print("--------------------------------------------------")
    print("Testing the   make_simple_string   function:")
    print("--------------------------------------------------")


def make_simple_string(m, n):
    """
    What comes in:
      -- a positive integer m
      -- a positive integer n that is >= m
    What goes out:  Returns the STRING whose characters are
          m, m+1, m+2, ... n,
      each with a "-" character after it,
      where m and n are the given arguments.
    Side effects:   None.
    Examples:
      If m is 5 and n is 13, then this function returns:
        "5-6-7-8-9-10-11-12-13-"

      If m and n are both 205, then this function returns:  "205-"

    Type hints:
      :type m: int
      :type n: int
    """
    # -------------------------------------------------------------------------
    # TODO: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    # -------------------------------------------------------------------------


def run_test_make_less_simple_string():
    """ Tests the   make_less_simple_string    function. """
    # -------------------------------------------------------------------------
    # TODO: 6. Implement this TEST function.
    #   It TESTS the  make_less_simple_string  function defined below.
    #   Include at least **   2   ** tests.
    #
    # Use the same 4-step process as for previous TEST functions.
    # -------------------------------------------------------------------------
    print()
    print("--------------------------------------------------")
    print("Testing the   make_less_simple_string   function:")
    print("--------------------------------------------------")


def make_less_simple_string(m, n):
    """
    What comes in:
      -- a positive integer m
      -- a positive integer n that is >= m
    What goes out:  The same as the previous problem,
      but WITHOUT the hyphen after the LAST number.
      That is, this function returns the STRING whose characters are
        m, m+1, m+2, ... n,
      with a "-" character BETWEEN each of the items
      and where m and n are the given arguments.
    Side effects:   None.
    Examples:
      If m is 5 and n is 13, then this function returns:
        "5-6-7-8-9-10-11-12-13"

      If m and n are both 205, then this function returns:  "205"

    Type hints:
      :type m: int
      :type n: int
    """
    # -------------------------------------------------------------------------
    # TODO: 7. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    # -------------------------------------------------------------------------


def run_test_draw_shapes():
    """ Tests the   draw_shapes    function. """
    print()
    print("-----------------------------------------------------------")
    print("Testing the   draw_shapes   function:")
    print("-----------------------------------------------------------")
    print("See the graphics window that pops up.")
    print("It should show 3 circles: red, white and blue.")
    print()
    print("Then it should ask the user to click the mouse to continue.")
    print("Then it should show 4 more shapes: a green circle,")
    print("  a yellow rectangle, a red circle and a thick black line.")

    # -------------------------------------------------------------------------
    # Test 1 is ALREADY DONE (here).
    # -------------------------------------------------------------------------
    window = rg.RoseWindow(500, 330, "draw_shapes, two tests")
    circles = [rg.Circle(rg.Point(50, 50), 50),
               rg.Circle(rg.Point(120, 50), 20),
               rg.Circle(rg.Point(250, 170), 130)]

    circles[0].fill_color = "red"
    circles[1].fill_color = "white"
    circles[2].fill_color = "blue"

    draw_shapes(circles, window)
    window.continue_on_mouse_click()

    # -------------------------------------------------------------------------
    # Test 2 is ALREADY DONE (here).
    # It runs in the same window as Test 1.
    # The bottom circle should appear only PARTIALLY in the window;
    # that is purposeful.
    # -------------------------------------------------------------------------
    rect_width = 100
    rect_height = 160
    rect_center = rg.Point(350, 100)
    various = [rg.Circle(rg.Point(400, 50), 30),
               rg.Rectangle(rg.Point(rect_center.x - rect_width / 2,
                                     rect_center.y - rect_height / 2),
                            rg.Point(rect_center.x + rect_width / 2,
                                     rect_center.y + rect_height / 2)),
               rg.Circle(rg.Point(400, 300), 80),
               rg.Line(rg.Point(0, 0), rg.Point(100, 330))]
    various[0].fill_color = "green"
    various[1].fill_color = "yellow"
    various[2].fill_color = "red"
    various[3].thickness = 10

    draw_shapes(various, window)

    window.close_on_mouse_click()


def draw_shapes(shapes, window):
    """
    What comes in:
      -- a sequence of rg.Shape objects
           Note: rg.Line, rg.Circle, rg.Point, ... are all rg.Shape
           objects.
      -- an rg.RoseWindow
    What goes out: Nothing (i.e., None).
    Side effects:
      See   draw_shapes.pdf   in this project for pictures
      that may help you better understand the following:

      For each rg.Shape in the given sequence of rg.Shape objects,
        1. Attaches the rg.Shape to the given rg.RoseWindow.
        2. Renders the rg.RoseWindow with a 0.3 second delay
             after the render.

    Examples:
      See the   draw_shapes.pdf   file in this project.
    Type hints:
      :type shapes:  list | tuple of rg._Shape
      :type window:  rg.RoseWindow
    """
    # -------------------------------------------------------------------------
    # TODO: 9. Implement and test this function.
    #             *** Make sure you do _TODO_ 8 in main first! ***
    #   The testing code is already written for you;
    #   you enabled it via _TODO_ 8.
    #  ########################################################################
    #  IMPORTANT: the same
    #      attach_to
    #  method works for ALL the rosegraphics shapes!
    #  FWIW: The word for ideas like this is "polymorphism".
    #  ########################################################################
    # -------------------------------------------------------------------------


def run_test_rectangles_from_circles():
    """ Tests the   rectangles_from_circles    function. """
    print()
    print("-----------------------------------------------------------")
    print("Testing the   rectangles_from_circles   function:")
    print("-----------------------------------------------------------")
    print("See the graphics window that pops up.")
    print("It should show circles, then the circles circumscribed,")
    print("then more circles, then the new circles circumscribed too.")
    print()
    print("See   rectangles_from_circles.pdf   in this project")
    print("for pictures of the anticipated results.")

    # -------------------------------------------------------------------------
    # Test 1 is ALREADY DONE (here).
    # -------------------------------------------------------------------------
    window = rg.RoseWindow(650, 350,
                           "rectangles_from_circles, two tests")
    circles = [rg.Circle(rg.Point(50, 80), 40),
               rg.Circle(rg.Point(150, 50), 30),
               rg.Circle(rg.Point(300, 100), 50),
               rg.Circle(rg.Point(220, 70), 60)]
    circles[0].fill_color = "red"
    circles[1].fill_color = "white"
    circles[2].fill_color = "blue"
    circles[3].fill_color = "green"

    # -------------------------------------------------------------------------
    # This test calls the   draw_shapes   function that YOU write,
    # above.  So if your   draw_shapes   breaks, so will this test.
    # -------------------------------------------------------------------------
    draw_shapes(circles, window)

    message = "The circles to be circumscribed are shown above."
    message = message + "  Click to continue."
    window.continue_on_mouse_click(message)

    rectangles = rectangles_from_circles(circles)

    if rectangles is None:
        print()
        print("Either you have not yet gotten")
        print("  to the   rectangles_from_circles  problem (OK, no problem)")
        print("  or you have forgotten to return a result from that function.")
        window.close_on_mouse_click()
        return

    draw_shapes(rectangles, window)
    message = "Now you should see the circumscribing rectangles too."
    message = message + "  Click to continue."

    window.continue_on_mouse_click(message)

    # -------------------------------------------------------------------------
    # Test 2 is ALREADY DONE (here).
    # It runs in the same window as Test 1.
    # -------------------------------------------------------------------------
    circles = []
    center = rg.Point(50, 150)
    radius = 35
    for _ in range(10):
        circle = rg.Circle(center, radius)
        circle.fill_color = "magenta"
        circles = circles + [circle]
        center.x = center.x + 2 * radius
        center.y = center.y + 15
        radius = radius - 3

    draw_shapes(circles, window)
    message = "More circles to be circumscribed are shown above."
    message = message + "  Click to continue."
    window.continue_on_mouse_click(message)

    rectangles = rectangles_from_circles(circles)

    draw_shapes(rectangles, window)
    message = "Now you should see the circumscribing rectangles too."
    message = message + "  Click to exit."

    window.continue_on_mouse_click(message, close_it=True)


def rectangles_from_circles(circles):
    """
    See   rectangles_from_circles.pdf   in this project for pictures
    that may help you better understand the following specification:

    What comes in:
      -- a sequence of rg.Circle objects
    What goes out:
      Returns a list of rg.Rectangles, where each rg.Rectangle circumscribes
      its corresponding rg.Circle in the given list of rg.Circles.
    Side effects: None.
    Examples: See   rectangles_from_circles.pdf   in this project.
    Type hints:
      :type circles:  list | tuple of rg.Circle
      :rtype: list of rg.Rectangles
    """
    # -------------------------------------------------------------------------
    # TODO: 10. Implement and test this function.
    #     The testing code is already written for you (above).
    #  ########################################################################
    #  IMPORTANT: Examine the testing code above carefully.  Be sure
    #             that you understand WHY the tests are adequate tests!
    #  ___
    #  IMPORTANT: The specification does NOT say to draw anything
    #            in this function, so DON'T draw anything in here!
    #  ########################################################################
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
