
## Note
# This code is build with klayout 0.29.6
# to use this code, you must install "klayout" 
# if you don't have "klayout", you can install it first
# by the command "pip install klayout"

# more detail please refer to https://pypi.org/project/klayout/

# more information about how to use python code to make a mask, you 
# can refer to following websites:
# https://www.klayout.de/doc-qt5/programming/python.html
# https://www.klayout.org/klayout-pypi/  (old version?)


## Purpose
# This is a tool to generate a mask of die numbers
# die number is combined by die ID and reticle ID
#   die ID: the coordinate of a die in a reticle
#   reticle ID: the coordinate of a reticle in whole wafer

# The coordinate system is shown in the picture below:
# (0, 0)
#    |-----------> x
#    |
#    |
#    |
#    V
#    y




import klayout.pya as pya
from number.number import *


# geometry define
number_of_reticles  = 10
number_of_dies      = 21


# setting the dimension of die and reticle
# unit: um
die_size            = 100
reticle_size        = die_size * number_of_dies


# setting the coordinate of each number
# unit: number
die_ID_x_tens       = Coordinate(10, -15)
die_ID_x_ones       = Coordinate(15, -15)
die_ID_y_tens       = Coordinate(70, -15)
die_ID_y_ones       = Coordinate(75, -15)

reticle_ID_x_tens   = Coordinate(10, -85)
reticle_ID_x_ones   = Coordinate(15, -85)
reticle_ID_y_tens   = Coordinate(70, -85)
reticle_ID_y_ones   = Coordinate(75, -85)


# define skip dies (test keys)
test_keys = [(0, 0),
             (20, 0),
             (0, 20), 
             (20, 20), 
             (19, 20)]




# create a new layout
layout = pya.Layout()

# create a new cell
top = layout.create_cell("ID")

# create new layers
layer_mark = layout.layer(0, 0)

# import number from file
numbers = import_number(layout, 'numbers.gds')



# insert numbers and rectangle marks
for i_reticle in range(number_of_reticles):
    for j_reticle in range(number_of_reticles):
        
        # set coordinate of reticle
        reticle = Coordinate(i_reticle * reticle_size, -j_reticle * reticle_size)

        # insert a DBox object by 4 points
        # DBox is a rectangle accept float number
        top.shapes(layer_mark).insert(pya.DBox(reticle.x, 
                                               reticle.y - reticle_size, 
                                               reticle.x + reticle_size, 
                                               reticle.y))

        for i_die in range(number_of_dies):
            for j_die in range(number_of_dies):

                # set coordinate of die
                die = Coordinate(i_die * die_size, -j_die * die_size)
                
                # ignore test keys
                if is_test_key(test_keys, i_die, j_die):
                    pass
                    
                # insert ID
                else:
                    # insert die ID
                    # x
                    x_tens, x_ones = two_digit_number_split(i_die)
                    insert_number(top, numbers, x_tens, reticle, die, die_ID_x_tens)
                    insert_number(top, numbers, x_ones, reticle, die, die_ID_x_ones)
                    
                    # y
                    y_tens, y_ones = two_digit_number_split(j_die)
                    insert_number(top, numbers, y_tens, reticle, die, die_ID_y_tens)
                    insert_number(top, numbers, y_ones, reticle, die, die_ID_y_ones)


                    # insert reticle ID
                    # x
                    x_tens, x_ones = two_digit_number_split(i_reticle)
                    insert_number(top, numbers, x_tens, reticle, die, reticle_ID_x_tens)
                    insert_number(top, numbers, x_ones, reticle, die, reticle_ID_x_ones)
                    
                    # y
                    y_tens, y_ones = two_digit_number_split(j_reticle)
                    insert_number(top, numbers, y_tens, reticle, die, reticle_ID_y_tens)
                    insert_number(top, numbers, y_ones, reticle, die, reticle_ID_y_ones)

                    

# save file as *.gds
layout.write("ID.gds")





