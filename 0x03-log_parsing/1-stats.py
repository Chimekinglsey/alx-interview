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

def log_parse() -> None:
    """ A function that reads stdin line by line and computes metrics """
    while True:
        usage = '<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>'
        line_count = 0
        total_f_size = 0
        status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
        status_code_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
        try:
            for line in sys.stdin:
                if not match(line):
                    continue  # Skip lines that don't match the format
                
                a, b, c, d, e, f, g, status_code, f_size = line.split()
                total_f_size += int(f_size)
                
                # Convert status_code to an integer
                status_code = int(status_code)
                
                if status_code in status_codes:
                    status_code_dict[str(status_code)] += 1
                
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
            exit(0)

if __name__ == '__main__':
    log_parse()
