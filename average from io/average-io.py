# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0.0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = int(line.find(':'))
    line = line[pos+1:pos+20]
    total += float(line)
    count += 1
    #print(total)
    #print(count)
    
print("Average spam confidence:", total/count)
