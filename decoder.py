# Find Valptr, Mincode, Maxcode from JpegSnoop (DHT) Huffman tables

# Huffman table
t = """Codes of length 01 bits (000 total): 
    Codes of length 02 bits (001 total): 00 
    Codes of length 03 bits (005 total): 01 02 03 04 05 
    Codes of length 04 bits (001 total): 06 
    Codes of length 05 bits (001 total): 07 
    Codes of length 06 bits (001 total): 08 
    Codes of length 07 bits (001 total): 09 
    Codes of length 08 bits (001 total): 0A 
    Codes of length 09 bits (001 total): 0B 
    Codes of length 10 bits (000 total): 
    Codes of length 11 bits (000 total): 
    Codes of length 12 bits (000 total): 
    Codes of length 13 bits (000 total): 
    Codes of length 14 bits (000 total): 
    Codes of length 15 bits (000 total): 
    Codes of length 16 bits (000 total):"""

# Split lines
lines = t.split("Codes of length")

# Matrix of separate values
lines2d = []

for line in lines[1::]:
    ar = []
    if line.strip()[line.find(":")::] == '':
        ar.append('')
    else:
        list = (line[line.find(": ") + 2::].strip()).split(" ")
        for val in list:
            ar.append(int(val, 16))
    lines2d.append(ar)

# Initialize three arrays
minval = [0]*16
maxval = [-1]*16
valptr = [0] * 16

# Initialize counter (valptr)
ctr = 0

# find valptrs
for i, line in enumerate(lines[1::]):
    num = line[line.find("(") + 1:line.find(" tot")]
    if len(num) == 0 or num == '000':
        continue
    valptr[i] = ctr
    ctr += int(num)

# Initialize counter (Min/Max val)
p = 0

# find Min/Max vals
for i, line in enumerate(lines2d):
    if len(line)==1 and line[0]=='' and i != 0:
        p = p - 1
        p = p+1
        p = p*2
        continue
    if len(line)==1 and line[0]=='' and i == 0:
        continue
    minval[i]=p
    p=p+len(line)-1
    maxval[i]=p
    p=2*(p+1)

# Print output
print("valptr: ")
print(valptr)
print("min: ")
print(minval)
print("max: ")
print(maxval)

# Sample output:

# valptr: 
# [0, 0, 1, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0, 0, 0, 0]
# min: 
# [0, 0, 2, 14, 30, 62, 126, 254, 510, 0, 0, 0, 0, 0, 0, 0]
# max: 
# [-1, 0, 6, 14, 30, 62, 126, 254, 510, -1, -1, -1, -1, -1, -1, -1]
