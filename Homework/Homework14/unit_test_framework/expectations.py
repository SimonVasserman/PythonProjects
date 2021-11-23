"""
This module contains functions of custom  Exception for checking tests of  Expect & Actual
"""

from unit_test_framework.helper import *


def ExpectEqual(actual, expected):
    """
    This function tests for strings and name
    If actual and expected match the test passed
    if not, there will be an error
    @param actual:  that will be testing
    @param expected: expect should be
    """
    line_number = GetParameter("TestLine")
    test_name = GetParameter("TestName")

    message = GetColor("NAME") + test_name() + "(" + GetColor("LINE") + f"line:{line_number()}" + GetColor(
        "NAME") + ") - \t"
    if actual == expected:
        message += GetColor("SUCCESS") + "SUCCESS"
    else:
        message += GetColor("FAILED") + f"FAILED: actual: {actual} , expected {expected}"
    print(message)


def ExpectNotEqual(actual, expected):
    """
   This function tests for strings and name
   If actual and expected  not match the test passed
   if not, there will be an error
    @param actual:  that will be testing
   @param expected: expect should be
   """
    line_number = GetParameter("TestLine")
    test_name = GetParameter("TestName")

    message = GetColor("NAME") + test_name() + "(" + GetColor("LINE") + f"line:{line_number()}" + GetColor(
        "NAME") + ") - \t"
    if not actual == expected:
        message += GetColor("SUCCESS") + "SUCCESS"
    else:
        message += GetColor("FAILED") + f"FAILED: actual: {actual} , expected {expected}"
    print(message)


def ExpectThrown(block, exception):
   """
    This function tests for strings and name
    If block, the test will be passed
     if not, there will be an error
    @param block: block the  program
    @param exception: type exceptions, else typing exception don't thrown.
   """
   line_number = GetParameter("TestLine")
   test_name = GetParameter("TestName")
   message = GetColor("NAME") + test_name() + "(" + GetColor("LINE") + f"line:{line_number()}" + GetColor(
       "NAME") + ") - \t"
   try:
       block()
   except type(exception):
       message += GetColor("SUCCESS") + "SUCCESS"
   else:
       message += GetColor("FAILED") + f" exception {type(exception)} don't thrown."
   print(message)




def ExpectNotThrown(block):
    """
       This function tests for strings and name
       If block, the test will blocked
       if not, test will be passed
        @param block: block the  program, typing exception don't thrown.
        @param exception: type exceptions, else typing success
       """
    line_number = GetParameter("TestLine")
    test_name = GetParameter("TestName")
    message = GetColor("NAME") + test_name() + "(" + GetColor("LINE") + f"line:{line_number()}" + GetColor(
        "NAME") + ") - \t"
    try:
        block()
    except Exception as e:
        message += GetColor("FAILED") + f" exception {e.__str__()} don't thrown."
    else:
        message += GetColor("SUCCESS") + "SUCCESS"
    print(message)
