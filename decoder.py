# Find Valptr, Mincode, Maxcode and Huffval from JpegSnoop (DHT) Huffman tables

# Huffman table
t = """Codes of length 01 bits (000 total): 
    Codes of length 02 bits (002 total): 01 02 
    Codes of length 03 bits (001 total): 03 
    Codes of length 04 bits (003 total): 04 11 05 
    Codes of length 05 bits (004 total): 12 06 21 07 
    Codes of length 06 bits (001 total): 13 
    Codes of length 07 bits (003 total): 22 00 08 
    Codes of length 08 bits (003 total): 31 14 41 
    Codes of length 09 bits (002 total): 32 23 
    Codes of length 10 bits (003 total): 15 09 51 
    Codes of length 11 bits (003 total): 42 16 61 
    Codes of length 12 bits (003 total): 24 33 17 
    Codes of length 13 bits (002 total): 52 71 
    Codes of length 14 bits (006 total): 81 18 62 91 25 43 
    Codes of length 15 bits (009 total): A1 B1 F0 26 34 72 0A 19 C1 
    Codes of length 16 bits (117 total): D1 35 27 E1 53 36 82 F1 92 A2 44 54 73 45 46 37 
                                         47 63 28 55 56 57 1A B2 C2 D2 E2 F2 64 83 74 93 
                                         84 65 A3 B3 C3 D3 E3 29 38 66 F3 75 2A 39 3A 48 
                                         49 4A 58 59 5A 67 68 69 6A 76 77 78 79 7A 85 86 
                                         87 88 89 8A 94 95 96 97 98 99 9A A4 A5 A6 A7 A8 
                                         A9 AA B4 B5 B6 B7 B8 B9 BA C4 C5 C6 C7 C8 C9 CA 
                                         D4 D5 D6 D7 D8 D9 DA E4 E5 E6 E7 E8 E9 EA F4 F5 
                                         F6 F7 F8 F9 FA"""



# Split lines
lines = t.split("Codes of length")

# Matrix of separate values
lines2d = []

for line in lines[1::]:
    line = line.replace('  ', '').replace('\n', '').replace('  ', ' ')
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

# Find HuffVals of table
huffvals = []
for val in lines2d:
    for val2 in val:
        if  val2 != '':
            huffvals.append(val2)
        # else:
        #     huffvals.append(0)

# Print output
print("valptr: " + str(valptr))
print("min: " + str(minval))
print("max: " + str(maxval))
print("Huffval: " + str(huffvals))

# Sample output:

# valptr: [0, 0, 2, 3, 6, 10, 11, 14, 17, 19, 22, 25, 28, 30, 36, 45]
# min: [0, 0, 4, 10, 26, 60, 122, 250, 506, 1016, 2038, 4082, 8170, 16344, 32700, 65418]
# max: [-1, 1, 4, 12, 29, 60, 124, 252, 507, 1018, 2040, 4084, 8171, 16349, 32708, 65534]
# Huffval: [1, 2, 3, 4, 17, 5, 18, 6, 33, 7, 19, 34, 0, 8, 49, 20, 65, 50, 35, 21, 9, 81, 66, 22, 97, 36, 51, 23, 82, 113, 129, 24, 98, 145, 37, 67, 161, 177, 240, 38, 52, 114, 10, 25, 193, 209, 53, 39, 225, 83, 54, 130, 241, 146, 162, 68, 84, 115, 69, 70, 55, 71, 99, 40, 85, 86, 87, 26, 178, 194, 210, 226, 242, 100, 131, 116, 147, 132, 101, 163, 179, 195, 211, 227, 41, 56, 102, 243, 117, 42, 57, 58, 72, 73, 74, 88, 89, 90, 103, 104, 105, 106, 118, 119, 120, 121, 122, 133, 134, 135, 136, 137, 138, 148, 149, 150, 151, 152, 153, 154, 164, 165, 166, 167, 168, 169, 170, 180, 181, 182, 183, 184, 185, 186, 196, 197, 198, 199, 200, 201, 202, 212, 213, 214, 215, 216, 217, 218, 228, 229, 230, 231, 232, 233, 234, 244, 245, 246, 247, 248, 249, 250]

