import klayout.pya as pya

# ========================================================================
class Coordinate:

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
# ========================================================================



# ========================================================================
def two_digit_number_split(number: int) -> tuple[int, int]:
    """
    Split two-digit number into tens and ones.

    Ex:
        input: 1
        output: (0, 0)

        input: 12
        output: (1, 2)
    """
    ones = number % 10
    tens = int( number / 10 )

    return tens, ones
# ========================================================================



# ========================================================================
def insert_number(cell, 
                  numbers: list, number: int, 
                  reticle: Coordinate, 
                  die: Coordinate, 
                  ID: Coordinate) -> None:

    """
    Insert a number into a cell.

    Variable:
        cell:       a cell to be appended number
        numbers:    a list of external cells of numbers
        number:     the number to be insert
        reticle:    the coordinate of upper-left corner of reticle
        die:        the coordinate of upper-left corner of die
        ID:         the coordinate of upper-left corner of ID
    """
    x = reticle.x + die.x + ID.x
    y = reticle.y + die.y + ID.y
    

    print(f"add number {number}")
    try:
        cell.insert(pya.DCellInstArray(numbers[number].cell_index(), 
                                       pya.DTrans(pya.DTrans.R0, pya.DPoint(x, y))))
    except:
        print(f"Error: insert error, no such external cell. Reticle ({reticle.x}, {reticle.y}) / Die ({die.x}, {die.y})")
        pass
# ========================================================================
    


# ========================================================================
def import_number(layout, file_name: str) -> list:
    """
    Import number 0~9 from another gds file.

    Variable:
        layout:     the layout under operating
        file_name:  the gds file containing number 0~9
    """

    layout.read( file_name )
    
    numbers = []
    for i in range(10):

        cell_name = 'NUMBER_' + str(i)
        numbers.append( layout.cell(cell_name) )

    return numbers
# ========================================================================



# ========================================================================
def is_test_key(test_keys: list[tuple[int, int]], 
                i: int, 
                j: int) -> bool:
    """
    Judge if the die is a test key

    Variable:
        test_keys: a list of tuples
        i: index of die in x direction
        j: index of die in y direction
    """
    for t in test_keys:

        if i == t[0] and j == t[1]:
            
            return True
# ========================================================================


