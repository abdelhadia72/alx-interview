#!/usr/bin/python3

"""
    file stats
"""
import sys
import re
import signal

stdin_fileno = sys.stdin

pattern = r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\] \"GET \/projects\/\d+ HTTP\/1\.1\" (\d{3}) (\d+)$"
status_objects = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0}


tracker = 0
file_size = 0
interrupt = False

for line in stdin_fileno:
    sline = line.strip()
    if tracker == 10:
        print(f"File size: {file_size}")
        for key, value in status_objects.items():
            if value != 0:
                print("{}: {}".format(key, value))
        tracker = 0

    if (re.match(pattern, sline)):
        status_objects[int(re.match(pattern, sline).group(3))] += 1
        file_size += int(re.match(pattern, sline).group(4))
        tracker += 1
    else:
        print("we get something doesn't match")
