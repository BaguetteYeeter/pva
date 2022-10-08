address += 1
high = ord(ram[address])
address += 1
low = ord(ram[address])

jmpaddress = low + (high * 0x100)

if ord(c[1]) == 0x02:
    address = jmpaddress - 1
