from validators import valid

def test_valid1():
    assert valid("malan@harvard.edu") == "This is a valid email address"

def test_valid2():
    assert valid("bhat.tushar@outlook.com") == "This is a valid email address"

def test_valid3():
    assert valid("malan@@@harvard.edu") == "This is not a valid email address"

def test_valid4():
    assert valid("bhat.tushar@outlook..com") == "This is not a valid email address"