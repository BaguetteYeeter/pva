address += 1
high = ord(ram[address])
address += 1
low = ord(ram[address])

movaddress = low + (high * 0x100)

c = list(c)
c[1] = ram[movaddress]
c = "".join(c)
