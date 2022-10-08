address += 1
high = ord(ram[address])
address += 1
low = ord(ram[address])

subA = ord(ram[low + (high * 0x100)])

a = list(a)
subB = ord(a[1]) + (ord(a[0]) * 0x100)

subbed = subB - subA

subHex = list(str(hex(subbed)))
while len(subHex) < 6:
    subHex.insert(2, "0")
a[0] = chr(int("".join(subHex[-4:-2]), 16))
a[1] = chr(int("".join(subHex[-2:]), 16))
a = "".join(a)