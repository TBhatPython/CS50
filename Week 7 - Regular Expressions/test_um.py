from um import count

def test_count1():
    assert count("um") == 1

def test_count2():
    assert count("um?") == 1

def test_count3():
    assert count("Um, thanks for the album.") == 1

def test_count4():
    assert count("Um, thanks, um...") == 2