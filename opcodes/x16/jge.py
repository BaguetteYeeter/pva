address += 1
high = ord(ram[address])
address += 1
low = ord(ram[address])

jmpaddress = low + (high * 0x100)

if ord(c[1]) == 0x02 or ord(c[1]) == 0x01:
    address = jmpaddress - 1
