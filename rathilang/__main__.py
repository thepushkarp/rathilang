import sys
import rathilang

filename = sys.argv[-1]
sourcecode = rathilang.load_source(filename)

if sourcecode:
    rathilang.evaluate(sourcecode)
