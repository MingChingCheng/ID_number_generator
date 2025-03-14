# ID number generator

This program is build with klayout 0.29.6.
This program generate the die ID and reticle ID on the wafer map.

* die ID: the coordinate of a die in a reticle
* reticle ID: the coordinate of a reticle in whole wafer

## Install

To use this code, you must install "klayout".

```console
pip install klayout
```

More detail please refer to <https://pypi.org/project/klayout/>

More information about how to use python code to make a mask, you can refer to following websites:

* <https://www.klayout.de/doc-qt5/programming/python.html>
* <https://www.klayout.org/klayout-pypi/>  (old version)

## Note

The coordinate system is shown in the picture below:

```plain
  (0, 0)
     |-----------> x
     |
     |
     |
     V
     y
```

## Usage

* Setting the geometric of dies and reticle

```python
# geometry define
number_of_reticles  = 10
number_of_dies      = 21

# setting the dimension of die and reticle
# unit: um
die_size            = 100
reticle_size        = die_size * number_of_dies
```

* Setting the coordinates of ids

```python
die_ID_x_tens       = Coordinate(10, -15)
die_ID_x_ones       = Coordinate(15, -15)
die_ID_y_tens       = Coordinate(70, -15)
die_ID_y_ones       = Coordinate(75, -15)

reticle_ID_x_tens   = Coordinate(10, -85)
reticle_ID_x_ones   = Coordinate(15, -85)
reticle_ID_y_tens   = Coordinate(70, -85)
reticle_ID_y_ones   = Coordinate(75, -85)
```

* Define the coordinate of test key

```python
# define skip dies (test keys)
test_keys = [(0, 0),
             (20, 0),
             (0, 20), 
             (20, 20), 
             (19, 20)]
```

* Prepare numbers.gds
Prepare a file named "numbers.gds" with different number subcell.
The original point of each number is at left-upper.

![number_coordinate](https://github.com/user-attachments/assets/7cb8e671-4044-4544-95a9-61c31361fd59)

## Result

The "ID.gds" will be produced. Include the two layers.

One layer is for ID number.
Another layer is a dummy layer for alignment (typically layer: 0).

![Result_ID_gds](https://github.com/user-attachments/assets/ff696e67-63f3-4799-81e2-7577a6d97335)
