"""Q1: A Plus Abs B
Python's operator 'module' defines binary functions for Python's intrinsic arithmetic operators.
For example, calling operator '.add(2,3)' is equivalent to calling the expression 2 + 3; both will return 5.
Note that when the operator module is imported into the namespace, like at the top of hw01.py,
you can just call add(2,3) instead of operator.add(2,3).
Fill in the blanks in the following function for adding 'a' to the absolute value of b, without calling abs.
You may not modify any of the provided code other than the two blanks.
"""


from operator import add, sub


def a_plus_abs_b(a, b):
    """
    Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> a_plus_abs_b(-1, 4)
    3
    >>> a_plus_abs_b(-1, -4)
    3
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)


def a_plus_abs_b_syntax_check():
    """Check that you didn't change the return statement of a_plus_abs_b.

    >>> # You aren't expected to understand the code of this test.
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return f(a, b)']
    """
    # You don't need to edit this function. It's just here to check your work.