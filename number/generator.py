# Generate the ID number cells gds file


import klayout.pya as pya


# ========================================================================
class Font:
    def __init__(self, height: float, width: float, weight: float,
                 inner_corner: float, outer_corner: float) -> None:
        
        self.height = height
        self.width = width
        self.weight = weight
        self.inner_corner = inner_corner
        self.outer_corner = outer_corner
# ========================================================================



# ========================================================================
class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
# ========================================================================



# ========================================================================
def segment_coordinate(s: str, font: Font) -> tuple[Point, Point]:

    if s == "a":
        p1 = Point(0, -font.weight)
        p2 = Point(font.width, 0)
    elif s == "b":
        p1 = Point(font.width-font.weight, (-font.height-font.weight)/2)
        p2 = Point(font.width, 0)
    elif s == "c":
        p1 = Point(font.width-font.weight, -font.height)
        p2 = Point(font.width, (-font.height+font.weight)/2)
    elif s == "d":
        p1 = Point(0, -font.height)
        p2 = Point(font.width, -font.height+font.weight)
    elif s == "e":
        p1 = Point(0, -font.height)
        p2 = Point(font.weight, (-font.height+font.weight)/2)
    elif s == "f":
        p1 = Point(0, (-font.height-font.weight)/2)
        p2 = Point(font.weight, 0)
    elif s == "g":
        p1 = Point(0, (-font.height-font.weight)/2)
        p2 = Point(font.width, (-font.height+font.weight)/2)

    return p1, p2
# ========================================================================



# ========================================================================
def number_to_7_segments(number: int) -> str:
    if number == 0:
        segments = "abcdef"
    elif number == 1:
        segments = "bc"
    elif number == 2:
        segments = "abged"
    elif number == 3:
        segments = "abgcd"
    elif number == 4:
        segments = "fgbc"
    elif number == 5:
        segments = "afgcd"
    elif number == 6:
        segments = "afedcg"
    elif number == 7:
        segments = "abc"
    elif number == 8:
        segments = "abcdefg"
    elif number == 9:
        segments = "abcdfg"
    
    return segments
# ========================================================================



# ========================================================================
def draw_number(cell: pya.Cell,
                layer: int,
                number: int,
                font: Font) -> None:

    segments = number_to_7_segments(number)
    
    # draw each segment as box
    for s in segments:
        p1, p2 = segment_coordinate(s, font)
        box = pya.DBox(p1.x, p1.y, p2.x, p2.y)
        cell.shapes(layer).insert(box)
    
    # merge all shapes
    region = pya.Region(cell.shapes(layer))
    region = region.merge()

    # round corner
    region.round_corners(font.inner_corner*1000, font.outer_corner*1000, 64)

    # replace merged, rounded shape with old ones
    cell.clear()
    cell.shapes(layer).insert(region)
# ========================================================================


