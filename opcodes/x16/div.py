address += 1
high = ord(ram[address])
address += 1
low = ord(ram[address])

divA = ord(ram[low + (high * 0x100)])

a = list(a)
divB = ord(a[1]) + (ord(a[0]) * 0x100)

divided = int(divB / divA)

dividedHex = list(str(hex(divided)))
while len(dividedHex) < 6:
    dividedHex.insert(2, "0")
a[0] = chr(int("".join(dividedHex[-4:-2]), 16))
a[1] = chr(int("".join(dividedHex[-2:]), 16))
a = "".join(a)