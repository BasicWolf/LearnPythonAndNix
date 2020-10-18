from .grep import grep


def test_line_contains_pattern():
    assert grep('hello world', 'hello')


def test_pattern_not_found_in_line():
    assert not grep('hello world', 'abc')
