#!/bin/env python3
 
from PyPath.cell import Cell

from pyPath.PyPathUI.pathCanvas import build

def main():
    l_root = build()
    l_root.mainloop()

if __name__ == '__main__':
    main()