# -*- coding: utf-8 -*-

# Filename : main.py
# Author   : Hao Limin
# Date     : 2020-03-12
# Email    : haolimin01@sjtu.edu.cn
# Python   : 3.7.5
# Command  : python3 main.py

"""

Introduction
============

This is the entry point of PySpice.
PySpice is a circuit simulator that written by Python. The supported circuit
may contain resistor, capacitor, inductor, voltage source, current souurce,
VCVS, CCCS, VCCS, CCVS, diode, MOSFET, etc.

Modules
=======

GUI    : use PyQt5 package.
Parser : use pybison(a wrapper for flex/bison).
Solver :
Plot   :

"""

from PyQt5.QtWidgets import *
from gui.mainwindow import MainWindow

import sys


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("PySpice")
    window = MainWindow()
    window.resize(800, 600)
    app.exec_()


def entry_point():
    main()


if __name__ == '__main__':
    entry_point()
