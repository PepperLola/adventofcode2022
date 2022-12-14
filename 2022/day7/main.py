import sys
import time
import re
import itertools
from collections import defaultdict

# shared variables here
path = []
sizes = defaultdict(int)
available = 70000000
need_unused = 30000000
min_directory = available - need_unused

# part 1, takes in lines of file
def p1(lines):
    for line in lines:
        line = line.strip()
        if "cd" in line:
            if ".." in line:
                path.pop()
            else:
                new_folder = line.split(" ")[-1]
                path.append(new_folder)
        else:
            match = re.match(r"(\d+) (.*)", line)
            if match:
                size = int(match.group(1))
                for i in range(1, len(path) + 1):
                    sizes["/".join(path[:i])] += size

    return sum([k for k in sizes.values() if k < 100000])

# part 2, takes in lines of file
def p2(lines):
    used = sizes['/']
    s = [k[1] for k in sorted(sizes.items(), key=lambda kv: kv[1])]
    for k in s:
        if k > used - min_directory:
            return k
    return 0

filename = "input.txt"

if "test" in sys.argv:
    filename = "test.txt"

def format_time(time_ns):
    names = ["hr", "m", "s", "ms", "µs", "ns"]
    names.reverse()
    times = [
        time_ns % 1000,
        (time_ns // 1000) % 1000,
        (time_ns // (1000 * 10**3)) % 1000,
        (time_ns // (1000 * 10**6)) % 60,
        (time_ns // (1000 * 10**6) // 60) % 60,
        (time_ns // (1000 * 10**6) // 60 // 60) % 60
    ]
    for i in range(0, len(times)):
        if i < len(times) - 1:
            if times[i + 1] == 0:
                return "%s%s " % (times[i], names[i])
        else:
            return "%s%s " % (times[i], names[i])

with open(filename, "r") as f:
    lines = f.readlines()
    t = time.perf_counter_ns()
    a = p1(lines)
    dur = time.perf_counter_ns() - t

    print("\033[0;33m├ Part 1:\033[22m\033[49m \033[1;93m%s\033[0m \033[3mtook\033[23m \033[3;92m%s\033[0m" % (a, format_time(dur)))

    t = time.perf_counter_ns()
    a = p2(lines)
    dur = time.perf_counter_ns() - t
    print("\033[0;33m└ Part 2:\033[22m\033[49m \033[1;93m%s\033[0m \033[3mtook\033[23m \033[3;92m%s\033[0m" % (a, format_time(dur)))
