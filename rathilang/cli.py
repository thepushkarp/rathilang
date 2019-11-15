#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""rahilang.cli module.

Command Line Interface to rathilang.

Copyright (c) 2019 Pushkar Patel
"""

from __future__ import print_function

import argparse
import setup

import rathilang


def main():
    """Run application as a CLI executable"""
    arg_parser = argparse.ArgumentParser(
        prog="rathilang",
        description="a Rathilang interpreter written in Python",
        argument_default=argparse.SUPPRESS,
    )

    arg_parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s {0}".format(setup.__VERSION__),
    )
    arg_parser.add_argument("file", help="the path to the baka's file")

    args = arg_parser.parse_args()

    sourcecode = rathilang.load_source(args.file)

    if sourcecode:
        rathilang.evaluate(sourcecode)
    else:
        arg_parser.print_usage()


if __name__ == "__main__":
    main()
