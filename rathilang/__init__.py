#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""rathilang module.

A brainfuck derivative based on the the characteristics of Aashutosh Rathi.

Copyright (c) 2019 Pushkar Patel
"""

from __future__ import print_function

import sys
import os

from rathilang.interpreter import RathilangProgram


def load_source(file):
    if os.path.isfile(file):
        if os.path.splitext(file)[1] == ".baka":
            with open(file, "r") as rathilang_file:
                rathilang_data = rathilang_file.read()

            return rathilang_data

        else:
            print("rathilang: either the file or you are not baka enough.", file=sys.stderr)
            return False

    else:
        print("rathilang: file nahi mila. dhoondh warna pitega.", file=sys.stderr)
        return False


def evaluate(source):
    """Run Rathilang system."""

    program = RathilangProgram(source)
    program.run()
