def validate_x(isbn):
    if isbn.count('X') == 1 and isbn[-1] == 'X' and len(isbn) == 10:
        return isbn

def adding_x(check_digit):
    if 'X' == check_digit:
        return 10
    return int(check_digit)

def check_isbn_10(isbn):
    total = sum(index * int(value) for index, value in enumerate(isbn[::-1][1:],2)) + adding_x(isbn[-1])
    if total % 11:
        return "Invalid"
    return convert_isbn_10_to_isbn_30(isbn)

def check_isbn_13(isbn):
    total = sum(int(value) * 3 if index % 2 else int(value) for index, value in enumerate(isbn[:-1])) + adding_x(isbn[-1])
    if total % 10:
        return 'Invalid'
    return 'Valid'

def convert_isbn_10_to_isbn_30(isbn_10):
    isbn_13 = f'978{isbn_10[:-1]}'
    for check_digit in range(10):
        isbn = f'{isbn_13}{check_digit}'
        if check_isbn_13(isbn) == "Valid":
            return isbn

def isbn13(isbn):
    isbn = isbn.upper()
    if 'X' in isbn:
        isbn = str(validate_x(isbn))
    isbn_len = len(isbn)
    if isbn_len == 10:
        return check_isbn_10(isbn)
    if isbn_len == 13:
        return check_isbn_13(isbn)
    return "Invalid"

# print(isbn13("9780316066525"))
# print(isbn13("9783866155237"))
# print(isbn13("9780345453747"))
# print(isbn13("031606652X"))
# print(isbn13("9783876155237"))
# print(isbn13("0345453747"))
# print(isbn13("0316066524"))
# print(isbn13("3866155239"))
# print(isbn13("817450494X"))