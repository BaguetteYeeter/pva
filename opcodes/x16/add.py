address += 1
high = ord(ram[address])
address += 1
low = ord(ram[address])

addA = ord(ram[low + (high * 0x100)])

a = list(a)
addB = ord(a[1]) + (ord(a[0]) * 0x100)

added = addA + addB

addedHex = list(str(hex(added)))
while len(addedHex) < 6:
    addedHex.insert(2, "0")
a[0] = chr(int("".join(addedHex[-4:-2]), 16))
a[1] = chr(int("".join(addedHex[-2:]), 16))
a = "".join(a)