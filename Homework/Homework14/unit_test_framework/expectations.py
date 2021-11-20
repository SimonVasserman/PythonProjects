from unit_test_framework.helper import *

def ExpectEqual(actual, expected):
    line_numer = GetParameter("TestLine")
    test_name = GetParameter("TestName")

    message = GetColor("NAME") + test_name() + "(" + GetColor("LINE") + f"line:{line_numer()}" + GetColor("NAME") + ") - \t"
    if actual == expected:
        message += GetColor("SUCCESS") + "SUCCESS"
    else:
        message += GetColor("FAILED") + f"FAILED: actual: {actual} , expected {expected}"
    print(message)

def ExpectNotEqual(actual, expected):
    line_numer = GetParameter("TestLine")
    test_name = GetParameter("TestName")

    message = GetColor("NAME") + test_name() + "(" + GetColor("LINE") + f"line:{line_numer()}" + GetColor("NAME") + ") - \t"
    if not actual == expected:
        message += GetColor("SUCCESS") + "SUCCESS"
    else:
        message += GetColor("FAILED") + f"FAILED: actual: {actual} , expected {expected}"
    print(message)

def ExpectThrown(block, exception):
    line_numer = GetParameter("TestLine")
    test_name = GetParameter("TestName")
    message = GetColor("NAME") + test_name() + "(" + GetColor("LINE") + f"line:{line_numer()}" + GetColor("NAME") + ") - \t"
    try:
        block()
    except type(exception):
        message += GetColor("SUCCESS") + "SUCCESS"
    else:
        message += GetColor("FAILED") + f" exception {type(exception)} don't thrown."
    print(message)

def ExpectNotThrown(block):
    line_numer = GetParameter("TestLine")
    test_name = GetParameter("TestName")
    message = GetColor("NAME") + test_name() + "(" + GetColor("LINE") + f"line:{line_numer()}" + GetColor("NAME") + ") - \t"
    try:
        block()
    except Exception as e:
        message += GetColor("FAILED") + f" exception {e.__str__()} don't thrown."
    else:
        message += GetColor("SUCCESS") + "SUCCESS"
    print(message)