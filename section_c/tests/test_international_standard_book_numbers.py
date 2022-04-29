import pytest
from isbn.international_standard_book_numbers import (
    validate_x,
    adding_x,
    check_isbn_10,
    check_isbn_13,
    convert_isbn_10_to_isbn_30,
    isbn13
)

@pytest.mark.parametrize("input, expected",[
    ("031606652X", "031606652X"),
    ("0316066X52", None),
    ("978387615523X", None),
    ("X783876155237", None)
    ])
def test_number_contains_x_at_the_end(input, expected):
    assert validate_x(input) == expected, "X should be at the end only."


@pytest.mark.parametrize("input, expected", [("X", 10), ("4", 4), ("7", 7)])
def test_check_digit(input, expected):
    assert adding_x(input) == expected



@pytest.mark.parametrize("input, expected", [
    ("0316066524","9780316066525"),
    ("3866155239","9783866155237"),
    ("817450494X","9788174504944")
])
def test_convert_isbn_10_to_isbn_30(input, expected):
    assert convert_isbn_10_to_isbn_30(input) == expected


@pytest.mark.parametrize("input, expected",[
    ("031606652X", "Invalid"),
    ("0345453747", "Invalid"),
    ("3866155239", "9783866155237"),
    ("817450494X", "9788174504944")
])
def test_check_isbn_10(input, expected):
    assert check_isbn_10(input) == expected


@pytest.mark.parametrize("input, expected",[
    ("9780316066525", "Valid"),
    ("9783866155237", "Valid"),
    ("9780345453747", "Valid"),
    ("9783876155237", "Invalid"),
    ("9780316066524", "Invalid"),
    ("9783866155239", "Invalid")
])
def test_check_isbn_30(input, expected):
    assert check_isbn_13(input) == expected


@pytest.mark.parametrize("input, expected", [
    ("9780316066525", "Valid"),
    ("9783866155237", "Valid"),
    ("9780345453747", "Valid"),
    ("031606652X", "Invalid"),
    ("9783876155237", "Invalid"),
    ("0345453747", "Invalid"),
    ("0316066524", "9780316066525"),
    ("3866155239", "9783866155237"),
    ("817450494X", "9788174504944"),
])
def test_isbn13(input, expected):
    assert isbn13(input) == expected