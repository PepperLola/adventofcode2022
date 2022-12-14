import sys
import time

# shared variables here
elf_possible = ['A', 'B', 'C']
my_possible = ['X', 'Y', 'Z']

# part 1, takes in lines of file
def p1(lines):
    score = 0
    for line in lines:
        other = elf_possible.index(line[0])
        mine = my_possible.index(line[2])

        score += mine + 1
        if other == mine:
            score += 3
        elif (other + 1) % 3 == mine:
            score += 6

    return score

# part 2, takes in lines of file
def p2(lines):
    score = 0
    for line in lines:
        other = elf_possible.index(line[0])
        outcome = my_possible.index(line[2])

        if outcome == 0:
            score += (other - 1) % 3 + 1
        elif outcome == 1:
            score += other + 1 + 3 # bonus
        elif outcome == 2:
            score += (other + 1) % 3 + 1 + 6
    return score

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
