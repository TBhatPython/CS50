from seasons import time_converter, UserBirth

def test_time_converter1():
    assert time_converter("2022-12-30") == "five hundred and twenty-five thousand, six hundred minutes"

def test_time_converter2():
    assert time_converter("2021-12-30") == "one million, fifty-one thousand, two hundred minutes"

def test_time_converter3():
    assert time_converter("2006/02/03") == "Invalid format"



