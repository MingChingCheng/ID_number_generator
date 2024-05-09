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
    Split two-digit number into tens and ones
    ex:
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
def insert_number(top, numbers: list, number: int, reticle: Coordinate, die: Coordinate, coordinate: Coordinate) -> None:

    x = reticle.x + die.x + coordinate.x
    y = reticle.y + die.y + coordinate.y
    
    if number > 3:
        return None
    else:
        print(f"add number {number}")
        
        top.insert(pya.DCellInstArray(numbers[number].cell_index(),
                                  pya.DTrans(pya.DTrans.R0, pya.DPoint(x, y))))
# ========================================================================
    


# ========================================================================
def import_number(layout: pya.Layout, file_name: str) -> list:

    layout.read( file_name )

    numbers = []
    for i in range(10):
        cell_name = 'NUMBER_' + str(i)
        numbers.append( layout.cell(cell_name) )

    return numbers
# ========================================================================
