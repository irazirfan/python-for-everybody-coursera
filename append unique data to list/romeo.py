fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    temp = line.split()
    if temp not in lst:
        for word in temp:
            if word not in lst:
                lst.append(word)

lst.sort()
print(lst)
