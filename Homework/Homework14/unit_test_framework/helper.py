import inspect

def GetColor(color_name):
    assert color_name != "NAME" or color_name != "SUCCESS" or color_name != "FAILED" or color_name != "LINE"

    if color_name == "NAME":
        return '\033[95m'
    elif color_name == "SUCCESS":
        return '\033[92m'
    elif color_name == "FAILED":
        return '\033[91m'
    elif color_name == "LINE":
        return '\033[39m'

def GetParameter(param_name):
    assert param_name != "TestName" or param_name != "TestLine"

    if param_name == "TestName":
        return lambda: str(inspect.stack()[2][3])
    elif param_name == "TestLine":
        return lambda: str(inspect.stack()[2][2])