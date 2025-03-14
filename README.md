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
