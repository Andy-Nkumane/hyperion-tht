# International Standard Book Numbers

The International Standard Book Number (ISBN) is a unique identifying number given to each published book. ISBNs assigned after January 2007 are 13 digits long (ISBN-13), however books with 10-digit ISBNs are still in wide use.

## How to set up for the project

* Create a virtual environment for the project
* Run the following commands:
```
pip install -r requirements.txt
python setup.py develop
```
* To run tests run the following command:
```
pytest
```
## Space Complexity

For completion memory is required whenever a solution a to problem is written. Memory may be used fo the following:
* Variables
* Program instruction
* Execution

To execute and produce the result of the amount of memory used by an algorithm is `space complexity`.
```
space complexity = input space + auxilary space
```

### Memory usage during execution

Memory space used for three reasons during execution:
* Instruction space
    > Amount of memory used to store compiled versions of instructions
* Environmental stack
    > There are times when a function gets called from another function, thus, pushing the current variables onto the system stack. As they wait for further executions, then the the function call to the inside function is made.
* Data space
    > Amount of apce used by the variables and constants

## Worst case space complexity

* isbn13 -> 18 bytes
* validate_x -> 14 bytes
* check_isbn_10 -> 8 bytes
* convert_isbn_10_to_isbn_30 -> 34 bytes
* check_isbn_13 -> 8 bytes

Total = 82 bytes

The above is for a valid 10-digit ISBN containing an `X`.
