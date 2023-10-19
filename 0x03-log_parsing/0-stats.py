#!/usr/bin/python3
"""log parsing"""
import sys
import re


def match(x: str):
    ip_match = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - '
    date_match = r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] '
    stats_match = r'"GET /projects/260 HTTP/1\.1" \d{3} \d+'
    pattern = ip_match + date_match + stats_match
    return True if re.match(pattern, x) else False


def log_parse():
    while True:
        usage = '<IP Address> - [<date>] "GET /projects/260 HTTP/1.1"\
<status code> <file size>'
        line_count = 0
        total_f_size = 0
        status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
        status_code_dict = {'200': 0, '301': 0, '400': 0, '401': 0,
                            '403': 0, '404': 0, '405': 0, '500': 0}
        # sorted_s_code = sorted(status_code_dict)
        try:
            for line in sys.stdin:
                if match(line):
                    a, b, c, d, e, f, g, status_code, f_size = line.split()
                    total_f_size += int(f_size)
                    if status_code in str(status_codes):
                        for k, v in status_code_dict.items():
                            if k == status_code:
                                status_code_dict[status_code] += 1
                    line_count += 1
                    if line_count % 10 == 0:
                        print(f'File size: {total_f_size}')
                        for key, val in status_code_dict.items():
                            if val > 0:
                                print(f"{key}: {val}")

                else:
                    raise TypeError(usage)

        except KeyboardInterrupt as err:
            print(f'File size: {total_f_size}')
            for key, val in status_code_dict.items():
                if val > 0:
                    print(f"{key}, {val}")
            exit(1)


if __name__ == '__main__':
    log_parse()
