address += 1
high = ord(ram[address])
address += 1
low = ord(ram[address])

movaddress = low + (high * 0x100)

d = list(d)
d[0] = ram[movaddress]
d = "".join(d)
