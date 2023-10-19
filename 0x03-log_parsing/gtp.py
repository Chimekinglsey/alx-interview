import sys
import re
from collections import defaultdict

# Define regular expression pattern to extract information from each line
pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)')

# Initialize variables to store metrics
total_size = 0
status_code_count = defaultdict(int)

try:
    line_count = 0
    for line in sys.stdin:
        match = pattern.match(line)
        if match:
            ip, date, status_code, file_size = match.groups()
            status_code = int(status_code)
            file_size = int(file_size)
            
            # Update metrics
            total_size += file_size
            status_code_count[status_code] += 1
            
            line_count += 1

            # Print metrics after every 10 lines
            if line_count % 10 == 0:
                print("Total file size: File size: {}".format(total_size))
                for code in sorted(status_code_count.keys()):
                    if code in (200, 301, 400, 401, 403, 404, 405, 500):
                        print("{}: {}".format(code, status_code_count[code]))
        
except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print("\nKeyboard interruption received. Printing final statistics.")

# Print final statistics
print("Total file size: File size: {}".format(total_size))
for code in sorted(status_code_count.keys()):
    if code in (200, 301, 400, 401, 403, 404, 405, 500):
        print("{}: {}".format(code, status_code_count[code]))
