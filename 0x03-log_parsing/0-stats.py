#!/usr/bin/python3

"""
file stats
"""
import sys
import re
import signal

pattern = r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\] \"GET \/projects\/\d+ HTTP\/1\.1\" (\d{3}) (\d+)$"
status_objects = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}


def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)


def print_statistics():
    print(f"File size: {file_size}")
    for key in sorted(status_objects.keys()):
        if status_objects[key] != 0:
            print("{}: {}".format(key, status_objects[key]))


tracker = 0
file_size = 0
interrupt = False

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    sline = line.strip()

    if interrupt:
        print_statistics()
        interrupt = False
        file_size = 0
        status_objects = {
            200: 0,
            301: 0,
            400: 0,
            401: 0,
            403: 0,
            404: 0,
            405: 0,
            500: 0}
        continue

    if tracker == 10:
        print_statistics()
        tracker = 0

    match = re.match(pattern, sline)
    if match:
        status_code = int(match.group(3))
        if status_code in status_objects:
            status_objects[status_code] += 1
        file_size += int(match.group(4))
        tracker += 1
    else:
        print("Line does not match expected pattern:", sline)
