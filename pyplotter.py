#!/usr/bin/env python

import argparse
import serial

try:
    import readline # noqa
except ImportError:
    pass

parser = argparse.ArgumentParser(
    description='CNC Import tool for Makeblock XY Plotter')
parser.add_argument('device', help="Serial device to connect")
parser.add_argument('-f', '--file',
                    help="File to send")
parser.add_argument('-b', '--baud', default=115200, help="Baud rate")


def main():
    arg = parser.parse_args()
    ser = serial.Serial(arg.device, arg.baud, timeout=1)
    wait_for(ser, "start")
    if not arg.file:
        while(True):
            inp = raw_input("> ")
            ser.write(inp)
    else:
        f = open(arg.file, 'r')
        for line in f:
            if line.rstrip() == "" or line.startswith("("):
                continue
            print "> %s" % line
            ser.write(line)
            wait_for(ser, "ok", "start")


def wait_for(ser, *args):
    line = ""
    while line not in args:
        line = ser.readline().rstrip()
        if line is not None and line != "":
            print "< %s" % line


if __name__ == "__main__":
    main()
