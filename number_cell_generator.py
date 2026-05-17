import klayout.pya as pya
from number.generator import draw_number
from number.generator import Font


# Setting GDS layer number and datatype
GDS_LAYER = 10
GDS_DATATYPE = 0

# Setting the font all unit in "um"
## size
height = 10        # height of the number
width = 5          # width of the number
weight = 1         # boldness of the number (or linewidth)

## round corner
inner_corner = 0.5   # inner corner rounded radius
outer_corner = 2   # outer corner rounded radius



if __name__ == "__main__":

    # define font object
    font = Font(height, width, weight, inner_corner, outer_corner)

    # create a new layout
    layout = pya.Layout()

    # create new layers for numbers
    layer = layout.layer(GDS_LAYER, GDS_DATATYPE)

    # create number cells from 0 to 9
    number_cells = []
    for i in range(10):
        number_cells.append(layout.create_cell(f"NUMBER_{i}"))

    # draw each number
    for i in range(10):
        draw_number(number_cells[i], layer, i, font)

    # save file as *.gds
    layout.write("numbers.gds")