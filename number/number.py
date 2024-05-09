import pya

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
    
    cell.insert(pya.DCellInstArray(numbers[number].cell_index(), 
                                   pya.DTrans(pya.DTrans.R0, pya.DPoint(x, y))))
    
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
