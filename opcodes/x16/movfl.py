address += 1
high = ord(ram[address])
address += 1
low = ord(ram[address])

movaddress = low + (high * 0x100)

f = list(f)
f[1] = ram[movaddress]
f = "".join(f)