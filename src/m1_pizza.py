"""
This module lets you practice:
  -- ITERATING (i.e. LOOPING) through a SEQUENCE
  -- Using OBJECTS
  -- DEFINING functions
  -- CALLING functions

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg
import math


def main():
    """ Calls the   TEST   functions in this module. """

    # ------------------------------------------------------------------
    # STUDENTS: Do the work in this module as follows.
    #   Otherwise, you will be overwhelmed by the output.
    #
    #   For each function that you implement:
    #     1. Locate the statements just below this comment that call TEST functions.
    #     2. UN-comment only one test at a time.
    #     3. Implement that function per its TO DO.
    #     4. When satisfied with your work, move onto the next test.
    # ------------------------------------------------------------------

    run_test_generate_points_on_circle()
    # run_test_draw_points_on_circle()
    # run_test_pizza()
    # run_test_polygon()
    # run_test_fancy_polygon()


def run_test_generate_points_on_circle():
    """ Tests the   generate_points_on_circle   function. """
    # ------------------------------------------------------------------
    # TODO: 2. Implement this TEST function.
    #   It TESTS the  generate_points_on_circle  function defined below.
    #   Include at least ** 1 ** ADDITIONAL test (that YOU write).
    #
    #   As usual, include both EXPECTED and ACTUAL results in your test
    #   and compute the latter BY HAND (not by running your program).
    #
    # Your professor may do this exercise with you as "live coding".
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   generate_points_on_circle   function:')
    print('--------------------------------------------------')

    # Test 1:
    expected = [rg.Point(125.0, 50.0),  # All numbers are approximate.
                rg.Point(112.5, 71.7),
                rg.Point(87.5, 71.7),
                rg.Point(75.0, 50.0),
                rg.Point(87.5, 28.3),
                rg.Point(112.5, 28.3)]
    circle = rg.Circle(rg.Point(100, 50), 25)
    answer = generate_points_on_circle(circle, 6)

    print('Expected:', expected)
    print('Actual:  ', answer)

    # ------------------------------------------------------------------
    # Test 2:  (YOU write THIS test)
    # ------------------------------------------------------------------


def generate_points_on_circle(circle_for_points, number_of_points_to_generate):
    """
    What comes in:
      -- an rg.Circle
      -- a positive integer that specifies how many rg.Points
           to generate
    What goes out:  Returns a list containing the given number
      of rg.Points, where the rg.Points:
      -- all lie on the circumference of the given rg.Circle,
      -- are equally distant from each other, and
      -- go clockwise around the circumference of the given rg.Circle,
            starting at the rightmost point on the rg.Circle.
    Side effects:   None.
    Examples:
      See the   'draw_points_on_circle'   pictures  in the   pizza.pdf
      file attached, with the points shown on those pictures.
    Type hints:
      :type circle_for_points:  rg.Circle
      :type number_of_points_to_generate: int
    """
    # ------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  generate_points_on_circle function -
    #     it has no TO DO.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # ------------------------------------------------------------------
    radius = circle_for_points.radius
    center_x = circle_for_points.center.x
    center_y = circle_for_points.center.y

    # ------------------------------------------------------------------
    # Each point is   delta_degrees   from the previous point,
    # along the circumference of the given circle.
    # ------------------------------------------------------------------
    delta_degrees = 360 / number_of_points_to_generate

    points = []
    degrees = 0
    for _ in range(number_of_points_to_generate):

        # --------------------------------------------------------------
        # Compute x and y of the point on the circumference of the
        # circle by using a polar representation.
        # --------------------------------------------------------------
        angle = math.radians(degrees)
        x = radius * math.cos(angle) + center_x
        y = radius * math.sin(angle) + center_y

        # --------------------------------------------------------------
        # Construct the point and append it to the list.
        # --------------------------------------------------------------
        point_on_circumference = rg.Point(x, y)
        points.append(point_on_circumference)

        # --------------------------------------------------------------
        # The next point will be    delta_degrees    from this point,
        # along the circumference of the given circle.
        # --------------------------------------------------------------
        degrees = degrees + delta_degrees

    return points


def run_test_draw_points_on_circle():
    """ Tests the   draw_points_on_circle   function. """
    # ------------------------------------------------------------------
    # TODO: 3. Implement this TEST function.
    #   It TESTS the   draw_points_on_circle   function defined below.
    #   Include at least ** 1 ** ADDITIONAL test (that YOU write).
    #
    #   As usual, include both EXPECTED and ACTUAL results in your test
    #   and compute the latter BY HAND (not by running your program).
    #
    # Your professor may do this exercise with you as "live coding".
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   draw_points_on_circle   function:')
    print('See the windows that pop up.')
    print('--------------------------------------------------')

    # Test 1:
    title = 'DRAW_POINTS_ON_CIRCLE, test 1:  7 yellow dots.'
    window = rg.RoseWindow(400, 400, title)
    circle = rg.Circle(rg.Point(200, 200), 150)
    draw_points_on_circle(window, circle, 7, 'yellow')
    window.close_on_mouse_click()

    # Tests 2 and 3 (on the same window):
    title = 'Tests 2 and 3:  6 blue on deep pink;  10 green1 on unfilled.'
    window = rg.RoseWindow(440, 400, title)
    circle = rg.Circle(rg.Point(135, 135), 50)
    circle.fill_color = 'deep pink'
    draw_points_on_circle(window, circle, 6, 'blue')
    window.continue_on_mouse_click()

    circle = rg.Circle(rg.Point(210, 210), 100)
    draw_points_on_circle(window, circle, 10, 'green1')
    window.close_on_mouse_click()

    # ------------------------------------------------------------------
    # Test 4:  (YOU write THIS test)
    # ------------------------------------------------------------------


def draw_points_on_circle(window, circle, number_of_points, color):
    """
    What comes in:
      -- an rg.RoseWindow
      -- an rg.Circle
      -- a positive integer that specifies how many rg.Points
           to generate and use as described below
      -- a string that can be used as a RoseGraphics color
    What goes out: Nothing (i.e., None).
    Side effects:
      See the 'draw_points_on_circle' pictures in   pizza.pdf   in this
      project; they may help you better understand the following:

      1. Attaches the given rg.Circle to the given rg.RoseWindow.
      2. Generates (constructs) the given number of rg.Point objects
           on the given rg.Circle's circumference,
           spaced equally from each other.
      3. For each of those rg.Point objects:
           a. Constructs an rg.Circle centered at that point,
              filled with the given color and with a radius of 10.
           b. Attaches the new rg.Circle to the given rg.RoseWindow.
           c. Attaches the rg.Point object to the given rg.RoseWindow.
      4. Renders the given rg.RoseWindow.

      Note that the rg.Point objects will be visible since each is
      attached AFTER its corresponding rg.Circle object, hence on TOP
      of its corresponding rg.Circle object.

    Examples:  See the   'draw_points_on_circle'   pictures
      in the   pizza.pdf   file in this project.
    Type hints:
      :type window:           rg.RoseWindow
      :type circle:           rg.Circle
      :type number_of_points: int
      :type color:            str
    """
    # ------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    # IMPLEMENTATION REQUIREMENT:
    #    You MUST USE (call) the   generate_points_on_circle
    #    (defined above) to generate the points to draw.
    #
    # Your professor may do this exercise with you as "live coding".
    # ------------------------------------------------------------------


def run_test_pizza():
    """ Tests the   pizza   function. """
    # ------------------------------------------------------------------
    # TODO: 5. Implement this TEST function.
    #   It TESTS the   pizza   function defined below.
    #   Include at least ** 1 ** ADDITIONAL test (that YOU write).
    #
    #   As usual, include both EXPECTED and ACTUAL results in your test
    #   and compute the latter BY HAND (not by running your program).
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   pizza   function:')
    print('See the windows that pop up.')
    print('--------------------------------------------------')

    # Test 1:
    title = 'PIZZA test 1:  5 slices, thin (thickness=3) blue lines.'
    window = rg.RoseWindow(400, 400, title)
    circle = rg.Circle(rg.Point(200, 200), 150)
    circle.outline_thickness = 3
    pizza(window, circle, 5, 'blue', 3)
    window.close_on_mouse_click()

    # Tests 2 and 3 (on the same window):
    title = 'PIZZA tests 2 and 3:  8 white slices on purple circle; 20 green slices on blue circle.'
    window = rg.RoseWindow(520, 400, title)

    circle = rg.Circle(rg.Point(125, 125), 50)
    circle.fill_color = 'purple'
    pizza(window, circle, 8, 'white', 5)
    window.continue_on_mouse_click()

    circle = rg.Circle(rg.Point(350, 200), 125)
    circle.fill_color = 'blue'
    pizza(window, circle, 20, 'green1', 3)

    window.close_on_mouse_click()

    # ------------------------------------------------------------------
    # Test 4:  (YOU write THIS test)
    #   SUGGESTION:  You might enjoy:
    #     -- a large number of thin black lines
    #     -- on a yellow-filled circle.
    # ------------------------------------------------------------------


def pizza(window, circle, number_of_slices, color, thickness):
    """
    What comes in:
      -- an rg.RoseWindow
      -- an rg.Circle
      -- an integer >= 2 that specifies how many rg.Lines
           to generate as described below
      -- a string that can be used as a RoseGraphics color
      -- a positive integer that specifies the thickness to be used
           for each rg.Line
    What goes out: Nothing (i.e., None).
    Side effects:
      See the   'pizza'   pictures in the   pizza.pdf   file in this
      project; they may help you better understand the following:

      1. Draws the given rg.Circle in the given rg.RoseWindow.
      2. Constructs and draws  rg.Line  objects to make the picture look
           like a 'pizza pie' cut into the given number of 'slices'.
         Each rg.Line has the given color and thickness (width).

    Examples:  See the   'pizza'   pictures in the   pizza.pdf   file
      in this project.
    Type hints:
      :type window:           rg.RoseWindow
      :type circle:           rg.Circle
      :type number_of_slices: int
      :type color:            str
      :type thickness:        int
    """
    # ------------------------------------------------------------------
    # TODO: 6. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    # IMPLEMENTATION REQUIREMENT:
    #    You MUST USE (call) the   generate_points_on_circle
    #    (defined above) to generate the relevant points,
    #    and then draw lines that are based in part on those points.
    # ------------------------------------------------------------------


def run_test_polygon():
    """ Tests the   polygon   function. """
    # ------------------------------------------------------------------
    # TODO: 7. Implement this TEST function.
    #   It TESTS the   polygon   function defined below.
    #   Include at least ** 1 ** ADDITIONAL test (that YOU write).
    #
    #   As usual, include both EXPECTED and ACTUAL results in your test
    #   and compute the latter BY HAND (not by running your program).
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   polygon   function:')
    print('See the windows that pop up.')
    print('--------------------------------------------------')

    # Tests 1 and 2 (on the same window):
    title = 'POLYGON tests 1 and 2:  3 segments with thick blue lines;  6 with medium red lines.'
    window = rg.RoseWindow(550, 400, title)

    circle = rg.Circle(rg.Point(100, 100), 80)
    circle.outline_thickness = 3
    polygon(window, circle, 3, 'blue', 10)
    window.continue_on_mouse_click()

    circle = rg.Circle(rg.Point(350, 200), 150)
    circle.outline_thickness = 3
    polygon(window, circle, 6, 'red', 5)

    window.close_on_mouse_click()

    # ------------------------------------------------------------------
    # Test 3:  (YOU write THIS test)
    # ------------------------------------------------------------------


def polygon(window, circle, number_of_segments, color, thickness):
    """
    What comes in:
      -- an rg.RoseWindow
      -- an rg.Circle
      -- an integer >= 2 that specifies how many rg.Lines
           to generate as described below
      -- a string that can be used as a RoseGraphics color
      -- a positive integer that specifies the thickness to be used
           for each rg.Line
    What goes out: Nothing (i.e., None).
    Side effects:
      See the   'polygon'   pictures in the   pizza.pdf   file in this
      project; they may help you better understand the following:

      1. Draws the given rg.Circle in the given rg.RoseWindow.
      2. Constructs and draws  rg.Line  objects that form
           a regular polygon with the given number of segments,
           inscribed in the given rg.Circle.
         Each rg.Line has the given color and thickness (width).

    Examples:  See the   'polygon'   pictures in the   pizza.pdf   file
      in this project.
    Type hints:
      :type window:             rg.RoseWindow
      :type circle:             rg.Circle
      :type number_of_segments: int
      :type color:              str
      :type thickness:          int
    """
    # ------------------------------------------------------------------
    # TODO: 8. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    # IMPLEMENTATION REQUIREMENT:
    #    You MUST USE (call) the   generate_points_on_circle
    #    (defined above) to generate the relevant points,
    #    and then draw lines that are based in part on those points.
    # ------------------------------------------------------------------


def run_test_fancy_polygon():
    """ Tests the   fancy_polygon   function. """
    # ------------------------------------------------------------------
    # TODO: 9. Implement this TEST function.
    #   It TESTS the   fancy_polygon   function defined below.
    #   Include at least ** 1 ** ADDITIONAL test (that YOU write).
    #
    #   As usual, include both EXPECTED and ACTUAL results in your test
    #   and compute the latter BY HAND (not by running your program).
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   fancy_polygon   function:')
    print('See the windows that pop up.')
    print('--------------------------------------------------')

    # Tests 1 and 2 (on the same window):
    title = 'FANCY POLYGON tests 1 and 2:  7 blue lines, hops = 2;  5 red lines, hops = 3.'
    window = rg.RoseWindow(520, 400, title)

    circle = rg.Circle(rg.Point(100, 100), 80)
    fancy_polygon(window, circle, 7, 2, 'blue', 3)
    window.continue_on_mouse_click()

    circle = rg.Circle(rg.Point(330, 200), 150)
    fancy_polygon(window, circle, 5, 3, 'red', 3)

    window.close_on_mouse_click()

    # Test 3 (on another window):
    title = 'FANCY POLYGON test 3:  20 lime green lines on blue circle, hops = 7.'
    window = rg.RoseWindow(480, 350, title)

    circle = rg.Circle(rg.Point(240, 165), 150)
    circle.fill_color = 'blue'
    fancy_polygon(window, circle, 20, 7, 'lime green', 5)
    window.close_on_mouse_click()

    # ------------------------------------------------------------------
    # Test 4:  (YOU write THIS test).
    #   If you wish, try even more tests to get some really cool
    #   pictures.  Some that I especially like are:
    #      -- 20 segments, hops of length 5
    #      -- 51 segments, hops of length 25
    #      -- 300 segments, hops of length 61
    #   For all these, filling the circles with one color and using
    #   a contrasting color for the lines makes them especially pretty.
    # ------------------------------------------------------------------


def fancy_polygon(window, circle, number_of_lines, hops_to_next_point, color, thickness):
    """
    What comes in:
      -- an rg.RoseWindow
      -- an rg.Circle
      -- an integer >= 2 that specifies how many rg.Lines
           to generate as described below
      -- a positive integer that specifies how many points each line
           "hops" over (see below for details).
      -- a string that can be used as a RoseGraphics color
      -- a positive integer that specifies the thickness to be used
           for each rg.Line
    What goes out: Nothing (i.e., None).
    Side effects:
      See the   'fancy_polygon'   pictures in the   pizza.pdf   file in
      this project; they may help you better understand the following:

      1. Draws the given rg.Circle in the given rg.RoseWindow.
      2. Constructs and draws   rg.Line   objects to make the picture
           look like an inscribed regular polygon with the given number
           of segments, but with each rg.Line going from one point
           on the given rg.Circle to the point on the given rg.Circle
           that is the given number of 'hops' away (wrapping as needed).
         Each rg.Line has the given color and thickness.
         Each rg.Line should be drawn as an arrow,
           by setting the rg.Line's   arrow   instance variable
           to the string   'last'.

         For example, if  hops_to_next_point   is 1,
            then the picture is a regular polygon.

         Or, if   hops_to_next_point is   2, the lines go:
           -- from point 0 to point 2
           -- from point 1 to point 3
           -- from point 2 to point 4
           -- from point 3 to point 5
           -- etc.

         One more example:
           if   hops_to_next_point   is 3
           and  number_of_segments   is 5, then the lines go:
           -- from point 0 to point 3
           -- from point 1 to point 4
           -- from point 2 to point 0 (note the 'wrap' effect)
           -- from point 3 to point 1
           -- from point 4 to point 2

    Examples:  See the   'fancy_polygon'   pictures in the   pizza.pdf
      file in this project.
    Type hints:
      :type window:          rg.RoseWindow
      :type circle:          rg.Circle
      :type number_of_lines: int
      :type hops_to_next_point: int
      :type color:           str
      :type thickness:       int
    """
    # ------------------------------------------------------------------
    # TODO: 10. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    # IMPLEMENTATION REQUIREMENT:
    #    You MUST USE (call) the   generate_points_on_circle
    #    (defined above) to generate the relevant points,
    #    and then draw lines that are based in part on those points.
    #
    ####################################################################
    # IMPORTANT: One way to do "wrapping" is to use the  %  operator
    #       appropriately.  ASK YOUR INSTRUCTOR FOR AN EXAMPLE.
    ####################################################################
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
