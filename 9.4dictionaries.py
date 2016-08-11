name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
#text = handle.read()

#words = list()
counts = dict()
for line in handle:
    word = line.split()
    if line.startswith("From"):
        counts[word[1]] = counts.get(word[1], 0) + 1
        
largest = 0
email = None
for k in counts:
    if counts[k] > largest:
        largest = counts[k]
        email = k
        
print email, largest
