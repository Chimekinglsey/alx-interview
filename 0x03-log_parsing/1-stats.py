#!/usr/bin/python3
"""Read from `stdin` and parse log"""
import datetime
import re
from time import sleep
from sys import argv


def match_ip(ip: str) -> bool:
    """checks ip address validity"""
    pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\d'
    result = re.match(pattern, ip)
    return True if result else False

usage = f'<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>'
if match_ip(argv[1]):
    ippaddr = argv[1]
else:
    raise TypeError(usage)
date, target = argv[2], argv[3]
stat_code, f_size = argv[4], argv[5]


def log_parse():
    """
    strict input format(Skip anything else):    
         <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
    """
    try:
        if len(argv) == 6:
            cum_f_size = 0
            status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
            count_scode = {200: 0, 301: 0, 400: 0, 401: 0,
                            403: 0, 404: 0, 405: 0, 500: 0}
            count_scode = dict(sorted(count_scode.items()))
            while True:
                cum_f_size += f_size
                print(f"File size: {cum_f_size}")
                if stat_code in status_codes and type(stat_code) is int:
                    count_scode[stat_code] += 1
                    for k,v in count_scode.items():
                        if v > 0:
                            print(f"{k}: {v}")
                sleep(10.0)
    except Exception as err:
        print(usage, '\n', err)
        
if __name__ == '__main__':
    log_parse()