#!/usr/bin/python3
"""log parsing"""
import sys
import re


def match(x: str) -> bool:
    """Checks for input match"""
    ip_match = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - '
    date_match = r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] '
    stats_match = r'"GET /projects/260 HTTP/1\.1" \d{3} \d+'
    pattern = ip_match + date_match + stats_match
    return True if re.match(pattern, x) else False


def log_parse():
    """parses logs from stdin"""
    status_code_dict = {'200': 0, '301': 0, '400': 0, '401': 0,
                        '403': 0, '404': 0, '405': 0, '500': 0
                        }
    try:
        total_f_size = 0
        line_count = 0
        for line in sys.stdin:
            a, b, c, d, e, f, g, status_code, f_size = line.split()
            total_f_size += int(f_size)

            if status_code in status_code_dict:
                status_code_dict[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print(f'File size: {total_f_size}')
                    for key, val in status_code_dict.items():
                        if val > 0:
                            print(f"{key}: {val}")

    except KeyboardInterrupt:
        print(f'File size: {total_f_size}')
        for key, val in status_code_dict.items():
            if val > 0:
                print(f"{key}: {val}")


if __name__ == '__main__':
    log_parse()
