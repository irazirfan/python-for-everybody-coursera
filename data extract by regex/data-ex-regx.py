import re
name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_621787.txt"
f = open(name)
sum = 0

for line in f:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    for s in stuff:
        if len(s) < 1:
            continue
        num = int(s)
        sum += num
print(sum)
