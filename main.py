import ast

ram = []
for i in range(0, 256):
    ram.append(chr(i))
ram = "".join(ram)
ram += chr(0x0)*0x0F00

mode = "x16"
prg = open("prg.hex", "rb").read()
codes = ast.literal_eval(open("opcodes/codes.json", "r").read())

for i in prg:
    ram += chr(i)

a = chr(0x0)*0x2
b = chr(0x0)*0x2
c = chr(0x0)*0x2
d = chr(0x0)*0x2
e = chr(0x0)*0x2
f = chr(0x0)*0x2

stack = []

address = 0x1000

while True:
    instruction = ord(ram[address])
    try:
        decode = codes[instruction]
    except KeyError:
        decode = "nop"

    exec(open("opcodes/"+mode+"/"+decode+".py", "r").read())
    #print(decode)
    #print(ram[0x0800])

    address += 0x1
