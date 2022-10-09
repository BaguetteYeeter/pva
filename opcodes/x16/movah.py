address += 1
high = ord(ram[address])
address += 1
low = ord(ram[address])

movaddress = low + (high * 0x100)

if high == 0xFF:
    regs = [a, a, b, c, d, e, f]
    register = regs[low]
    movaddress = ord(register[1]) + (ord(register[0]) * 0x100)

a = list(a)
a[0] = ram[movaddress]
a = "".join(a)
