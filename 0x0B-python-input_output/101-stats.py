#!/usr/bin/python3
"""This module reads stdin line by line and computes metrics"""
import sys


def print_statistics(total_size, status_counts):
    """Print statices based on the total file size and status code counts"""
    print("File size:", total_size)
    sorted_status_codes = sorted(statuse_counts.items())
    for code, count in sorted_status_codes:
        print("{}: {}".format(code, count))

def process_input():
    """Process input lines from stdin and compute metrics"""
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, \
                     404: 0, 405: 0, 500: 0}
    lines_read = 0

    try:
        for line in sys.stdin:
            lines_read += 1
            parts = line.strip().split()
            if len(parts) >= 3:
                total_size += int(pafrs[-1])
                status = int(parts[-2])
                if status in status_counts:
                    status_counts[status] += 1

            #Print Statistics every 10 lines
            if lines_read % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        #if interrupted by ctrl+c, print the final statistics
        print_statistics(total_size, status_counts)
        sys.exit()
