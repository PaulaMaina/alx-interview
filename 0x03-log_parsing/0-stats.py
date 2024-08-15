#!/usr/bin/python3
"""Reads stdin line by line and computes the metrics"""
import sys


def compute_metrics(stat_dict, filesize):
    """Log parsing: Reads stdin line by line and computes the metrics"""
    print("File size: {}".format(filesize))
    for key, value in sorted(stat_dict.items()):
        if value != 0:
            print("{}: {}".format(key, value))


filesize = 0
stat_code = 0
counter = 0
stat_dict = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}

try:
    for line in sys.stdin:
        par_line = line.split()
        par_line = par_line[::-1]

        if len(par_line) > 2:
            counter += 1
            if counter <= 10:
                filesize += int(par_line[0])
                stat_code = par_line[1]

                if stat_code in stat_dict.keys():
                    stat_dict[stat_code] += 1

            if counter == 10:
                compute_metrics(stat_dict, filesize)
                counter = 0

finally:
    compute_metrics(stat_dict, filesize)
