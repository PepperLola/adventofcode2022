import sys
import time
import re

# shared variables here
def build_crates(line, crates):
    last_idx = 0
    for i in range(0, len(line), 4):
        if line[i] != "[":
            continue
        idx = i // 4
        while len(crates) < idx + 1:
            crates.append([])
        crates[idx].append(line[i + 1])
    return crates

def top_crates(crates):
    res = ""
    for stack in crates:
        res += stack[0]
    return res

# part 1, takes in lines of file
def p1(lines):
    crates = []
    num_lines = len(str(lines))
    max_num_line_len = len(str(num_lines))
    for i in range(len(lines)):
        print(f"Processing line {str(i).zfill(max_num_line_len)}/{num_lines}", end="\r")
        line = lines[i]
        if '[' in line:
            crates = build_crates(line, crates)
        elif "move" in line:
            moves = re.findall("[0-9]+", line)
            amt = int(moves[0])
            chosen_crate = int(moves[1]) - 1
            dest_crate = int(moves[2]) - 1

            for i in range(amt):
                crates[dest_crate] = [crates[chosen_crate][0]] + crates[dest_crate]
                crates[chosen_crate] = crates[chosen_crate][1:]
                
    return top_crates(crates)

# part 2, takes in lines of file
def p2(lines):
    crates = []
    for line in lines:
        if '[' in line:
            crates = build_crates(line, crates)
        elif "move" in line:
            moves = re.findall("[0-9]+", line)
            amt = int(moves[0])
            chosen_crate = int(moves[1]) - 1
            dest_crate = int(moves[2]) - 1

            crates[dest_crate] = crates[chosen_crate][:amt] + crates[dest_crate]
            crates[chosen_crate] = crates[chosen_crate][amt:]
                
    return top_crates(crates)

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
