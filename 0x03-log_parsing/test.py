
# import signal
#
# def interrupt_handler(signum, frame):
#     print("SIGINT received. Exiting...")
#
# signal.signal(signal.SIGINT, interrupt_handler)
#
# while True:
#     pass
#

import sys
# # import re

# # pattern = r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\] \"GET \/projects\/\d+ HTTP\/1\.1\" (\d{3}) (\d+)$"

for line in sys.stdin:
    print(line.strip())
    # print(re.match(pattern, line))


# import sys

# result = ""
# for line in sys.stdin:
#     stripped = line.strip()
#     if stripped:
#         result += stripped
#     else:
#         result += "\n"

# print("File is being copied")
# with open("testResult.txt", "w") as file:
#     file.write(result)
# print("File copying is complete!")