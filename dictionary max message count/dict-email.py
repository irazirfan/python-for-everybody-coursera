name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    if not line.startswith("From "): continue
    words = line.split()
    emails = words[1]
    counts[emails] = counts.get(emails, 0) + 1
    
maxCount = None
maxEmail = None

for email,count in counts.items():
    if maxCount is None or count > maxCount:
        maxCount = count
        maxEmail = email

print(maxEmail, maxCount)
